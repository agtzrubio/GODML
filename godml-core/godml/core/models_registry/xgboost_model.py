import xgboost as xgb
from godml.core.metrics import evaluate_binary_classification

def train_model(X_train, y_train, X_test, y_test, params):
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    booster = xgb.train(params, dtrain, num_boost_round=100)

    # XGBoost ya devuelve probabilidades directamente
    preds = booster.predict(dtest)

    # Evalúa con las probabilidades
    metrics = evaluate_binary_classification(y_test, preds)

    return booster, preds, metrics


