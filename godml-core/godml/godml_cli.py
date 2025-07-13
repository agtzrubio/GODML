# Copyright (c) 2024 Arturo Gutierrez Rubio Rojas
# Licensed under the MIT License

import os
import typer
import shutil
from pathlib import Path
from godml.core.parser import load_pipeline
from godml.core.executors import get_executor
from godml.utils.logger import get_logger

logger = get_logger()

app = typer.Typer()

@app.command()
def run(file: str = typer.Option(..., "--file", "-f", help="Ruta al archivo YAML")):
    """
    Ejecuta un pipeline GODML desde un archivo YAML.
    """
    try:
        pipeline = load_pipeline(file)
        executor = get_executor(pipeline.provider)
        executor.validate(pipeline)
        result = executor.run(pipeline)
        
        if result is False:
            logger.error("❌ Entrenamiento fallido")
            raise typer.Exit(1)
            
    except Exception as e:
        logger.error(f"❌ Error: {str(e)}")
        raise typer.Exit(1)

@app.command()
def init(project_name: str):
    """
    Inicializa un nuevo proyecto GODML.
    """
    logger.info(f"🚀 Inicializando proyecto GODML: {project_name}")
 
    
    # Crear estructura de directorios
    project_path = Path(project_name)
    project_path.mkdir(exist_ok=True)
    
    # Crear subdirectorios
    (project_path / "data").mkdir(exist_ok=True)
    (project_path / "outputs").mkdir(exist_ok=True)
    (project_path / "models").mkdir(exist_ok=True)
    
    # Crear godml.yml template
    godml_template = f"""name: {project_name}
version: 1.0.0
provider: mlflow

dataset:
  uri: ./data/your_dataset.csv
  hash: auto

model:
  type: xgboost
  hyperparameters:
    max_depth: 5
    eta: 0.3
    objective: binary:logistic
    eval_metric: auc

metrics:
- name: auc
  threshold: 0.85
- name: accuracy
  threshold: 0.80

governance:
  owner: your-team@company.com
  tags:
  - project: {project_name}
  - environment: development

deploy:
  realtime: false
  batch_output: ./outputs/predictions.csv
"""
    
    # Escribir archivos
    with open(project_path / "godml.yml", "w") as f:
        f.write(godml_template)
    
    with open(project_path / "README.md", "w") as f: 
        f.write(f"# {project_name}\n\nProyecto GODML generado automáticamente.")
    
    with open(project_path / "requirements.txt", "w") as f:
        f.write("godml>=0.1.0\npandas>=1.3.0\nscikit-learn>=1.0.0\nxgboost>=1.5.0\nmlflow>=2.0.0")

    logger.info(f"✅ Proyecto {project_name} creado exitosamente!")
    logger.info(f"📁 Ubicación: {project_path.absolute()}")
    logger.info("📋 Próximos pasos:")
    logger.info(f"   cd {project_name}")
    logger.info("   pip install -r requirements.txt")
    logger.info("   godml run -f godml.yml")

def main():
    """Función principal para el CLI"""
    app()

if __name__ == "__main__":
    main()
