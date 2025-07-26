from godml.core.base_model_interface import BaseModel
import xgboost as xgb
from godml.core.metrics import evaluate_binary_classification

class XgboostModel(BaseModel):
    def __init__(self):
        self.model = None

    def train(self, X_train, y_train, X_test, y_test, params):
        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)

        self.model = xgb.train(params, dtrain, num_boost_round=100)
        preds = self.model.predict(dtest)

        metrics = evaluate_binary_classification(y_test, preds)

        return self.model, preds, metrics

    def predict(self, X):
        if self.model is None:
            raise ValueError("Modelo no entrenado aún.")
        
        dmatrix = xgb.DMatrix(X)
        return self.model.predict(dmatrix)
