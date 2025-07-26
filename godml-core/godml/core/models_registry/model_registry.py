from godml.core.models_registry.random_forest_model import train_model as rf_train
from godml.core.models_registry.xgboost_model import train_model as xgb_train
from godml.core.models_registry.logistic_regression_model import train as lr_train
from godml.core.models_registry.lightgbm_model import train as lgbm_train
from godml.core.models_registry.lstm_forecast_model import train as lstm_train

model_registry = {
    "random_forest": rf_train,
    "logistic_regression": lr_train,
    "lightgbm": lgbm_train,
    "lstm_forecast": lstm_train,
    "xgboost": xgb_train
}
