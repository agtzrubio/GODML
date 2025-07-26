import numpy as np
import pandas as pd
from typing import Dict
from sklearn.ensemble import RandomForestClassifier
from godml.core.base_model_interface import BaseModel
from godml.core.metrics import evaluate_binary_classification



class RandomForestModel(BaseModel):    
    # Solo los hiperparámetros válidos de RandomForest
    ALLOWED_PARAMS = {
        'n_estimators', 'criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf',
        'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease',
        'bootstrap', 'oob_score', 'n_jobs', 'random_state', 'verbose', 'warm_start',
        'class_weight', 'ccp_alpha', 'max_samples'
    }

    def __init__(self):
        self.model = None

    def train(self, X_train, y_train, X_test, y_test, params: Dict):
        # Filtra solo los parámetros válidos para RandomForest
        valid_params = {k: v for k, v in params.items() if k in self.ALLOWED_PARAMS}

        # 🌲 Entrenar RandomForest
        self.model = RandomForestClassifier(**valid_params)
        self.model.fit(X_train, y_train)

        # 🔮 Inferencia y evaluación
        preds = self.model.predict_proba(X_test)[:, 1]
        metrics = evaluate_binary_classification(y_test, preds)

        return self.model, preds, metrics

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        if self.model is None:
            raise ValueError("❌ El modelo no ha sido entrenado.")
        return self.model.predict_proba(X)[:, 1]


