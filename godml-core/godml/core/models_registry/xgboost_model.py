import xgboost as xgb

def train_model(X_train, y_train, X_test, y_test, params):
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    booster = xgb.train(params, dtrain, num_boost_round=100)
    preds = booster.predict(dtest)

    return booster, preds
