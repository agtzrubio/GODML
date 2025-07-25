import os
from pathlib import Path
from godml.notebook_api import GodmlNotebook
from godml.utils.model_storage import list_models

def test_model_is_saved(tmp_path):
    # Preparar dataset temporal
    data_path = tmp_path / "data"
    data_path.mkdir()
    csv_path = data_path / "churn.csv"

    import pandas as pd
    from sklearn.datasets import make_classification
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(4)])
    df["target"] = y
    df.to_csv(csv_path, index=False)

    # Crear y entrenar pipeline
    godml = GodmlNotebook()
    godml.create_pipeline(
        name="test_model_save",
        model_type="random_forest",
        hyperparameters={"max_depth": 3},
        dataset_path=str(csv_path)
    )
    godml.train()

    # Guardar modelo
    model_name = "pytest_rf_model"
    godml.save_model(model_name=model_name, environment="experiments")

    # Validaciones
    env_path = Path("models/experiments")
    assert (env_path / f"{model_name}_latest.pkl").exists()
    assert (env_path / f"{model_name}_metadata.json").exists()

    # Confirmar que aparece en la lista
    models = list_models("experiments")
    assert model_name in models
