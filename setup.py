from setuptools import setup, find_packages

setup(
    name="godml",
    version="0.1.0",
    description="Governed, Observable & Declarative Machine Learning CLI",
    author="Arturo Gutierrez Rubio Rojas",
    license="MIT",
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
        "tensorflow",
    ],
    entry_points={
        "console_scripts": [
            "godml=godml.godml_cli:app",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
