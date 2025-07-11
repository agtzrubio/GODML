from setuptools import setup, find_packages

setup(
    name="godml",
    version="0.1.0",
    description="Governed, Observable & Declarative Machine Learning CLI",
    author="Arturo",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer[all]",
        "pydantic",
        "mlflow",
        "pandas",
        "scikit-learn",
        "xgboost",
        "lightgbm",
        "tensorflow",  # opcional, si usarás keras
        # agrega otras dependencias que uses en godml
    ],
    entry_points={
        "console_scripts": [
            "godml=godml.godml_cli:app",
        ],
    },
    python_requires=">=3.8",
)
