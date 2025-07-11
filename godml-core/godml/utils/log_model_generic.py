import mlflow
import mlflow.sklearn
import mlflow.xgboost
import mlflow.lightgbm
from tensorflow import keras

from sklearn.base import BaseEstimator
from xgboost import Booster as XGBBooster
from lightgbm import Booster as LGBMBooster
from tensorflow.keras.models import Model as KerasModel

def log_model_generic(model, model_name: str = "model", registered_model_name: str = None):
    """
    Registra un modelo de forma genérica detectando el framework usado (XGBoost, LightGBM, sklearn, Keras).
    """
    if isinstance(model, XGBBooster):
        mlflow.xgboost.log_model(model, model_name, registered_model_name=registered_model_name)
    elif isinstance(model, LGBMBooster):
        mlflow.lightgbm.log_model(model, model_name, registered_model_name=registered_model_name)
    elif isinstance(model, BaseEstimator):
        mlflow.sklearn.log_model(model, model_name, registered_model_name=registered_model_name)
    elif isinstance(model, KerasModel):
        mlflow.keras.log_model(model, model_name, registered_model_name=registered_model_name)
    else:
        raise NotImplementedError(f"Modelo de tipo {type(model)} no soportado por log_model_generic.")
