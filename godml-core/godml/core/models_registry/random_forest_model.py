from typing import Dict
from sklearn.ensemble import RandomForestClassifier
from godml.core.metrics import evaluate_binary_classification


# Solo los hiperparámetros válidos de RandomForest
ALLOWED_PARAMS = {
    'n_estimators', 'criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf',
    'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease',
    'bootstrap', 'oob_score', 'n_jobs', 'random_state', 'verbose', 'warm_start',
    'class_weight', 'ccp_alpha', 'max_samples'
}

def train_model(X_train, y_train, X_test, y_test, params: Dict):
    # Filtra solo los parámetros válidos para RandomForest
    valid_params = {k: v for k, v in params.items() if k in ALLOWED_PARAMS}
    
    clf = RandomForestClassifier(**valid_params)
    clf.fit(X_train, y_train)
    
    preds = clf.predict_proba(X_test)[:, 1]    
    metrics = evaluate_binary_classification(y_test, preds)
    
    return clf, preds, metrics


