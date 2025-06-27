import mlflow
import mlflow.xgboost
from godml.core.engine import BaseExecutor
from godml.core.models import PipelineDefinition
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import xgboost as xgb
import os

class MLflowExecutor(BaseExecutor):
    def __init__(self, tracking_uri: str = None):
        if tracking_uri:
            mlflow.set_tracking_uri(tracking_uri)
        mlflow.set_experiment("godml-experiment")

    def preprocess_for_xgboost(self, df, target_col="target"):
        if target_col not in df.columns:
            raise ValueError("El dataset debe contener una columna llamada 'target'.")
        # Mapear target a numérico si es object (por ejemplo, 'Yes'/'No')
        if df[target_col].dtype == object:
            df[target_col] = df[target_col].map({"Yes": 1, "No": 0})
        
        y = df[target_col]
        X = df.drop(columns=[target_col])

        # One-hot encode columnas categóricas (object o category)
        cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
        if cat_cols:
            X = pd.get_dummies(X, columns=cat_cols, drop_first=True)
        return X, y

    def run(self, pipeline: PipelineDefinition):
        print(f"🚀 Entrenando modelo con MLflow: {pipeline.name}")

        # Cargar dataset
        dataset_path = pipeline.dataset.uri
        if dataset_path.startswith("s3://"):
            raise ValueError("MLflowExecutor solo soporta datasets locales (CSV).")

        df = pd.read_csv(dataset_path)
        X, y = self.preprocess_for_xgboost(df, target_col="target")

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=max(0.5, 2 / len(X)), random_state=42, stratify=y
        )

        params = pipeline.model.hyperparameters.dict()
        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)

        with mlflow.start_run(run_name=pipeline.name):
            # Registrar dataset original como artifact para trazabilidad
            mlflow.log_artifact(dataset_path, artifact_path="dataset")

            # Registrar metadata de pipeline como tags en MLflow UI

            mlflow.set_tag("dataset.uri", pipeline.dataset.uri)
            mlflow.set_tag("dataset.version", pipeline.version)

            mlflow.set_tag("version", pipeline.version)
            if hasattr(pipeline, "description"):
                mlflow.set_tag("description", pipeline.description)
            if hasattr(pipeline.governance, "owner"):
                mlflow.set_tag("owner", pipeline.governance.owner)
            if hasattr(pipeline.governance, "tags"):
                for tag_dict in pipeline.governance.tags:
                    for k, v in tag_dict.items():
                        mlflow.set_tag(k, v)

            # Registrar cada hiperparámetro como parámetro en MLflow
            for param_name, param_value in params.items():
                mlflow.log_param(param_name, param_value)

            booster = xgb.train(params, dtrain, num_boost_round=100)

            # Agregar input_example y signature para trazabilidad y validación
            input_example = X_train.iloc[:5]
            signature = mlflow.models.signature.infer_signature(
                input_example,
                booster.predict(xgb.DMatrix(input_example))
            )

            mlflow.xgboost.log_model(
                booster,
                "model",
                input_example=input_example,
                signature=signature,
                registered_model_name="churn-xgboost-godml"
            )

            preds = booster.predict(dtest)
            auc = roc_auc_score(y_test, preds)
            mlflow.log_metric("auc", auc)

            print(f"✅ Entrenamiento finalizado. AUC: {auc:.4f}")

            # Validación del threshold
            expected_auc = pipeline.metrics[0].threshold
            if auc < expected_auc:
                raise ValueError(f"🚫 AUC ({auc:.4f}) por debajo del mínimo requerido ({expected_auc})")

            # Simulación de deploy batch (predicciones en archivo CSV)
            if pipeline.deploy.batch_output:
                os.makedirs(os.path.dirname(pipeline.deploy.batch_output), exist_ok=True)
                pd.DataFrame({"prediction": preds}).to_csv(pipeline.deploy.batch_output, index=False)
                print(f"📦 Predicciones guardadas en: {pipeline.deploy.batch_output}")

    def validate(self, pipeline: PipelineDefinition):
        from godml.core.validators import validate_pipeline
        warnings = validate_pipeline(pipeline)
        for w in warnings:
            print("⚠️", w)
