import typer
from godml.core.parser import load_pipeline
from godml.core.executors import get_executor

app = typer.Typer()

@app.command()
def run(file: str = typer.Option(..., "--file", "-f", help="Ruta al archivo YAML")):
    """
    Ejecuta un pipeline GODML desde un archivo YAML.
    """
    pipeline = load_pipeline(file)
    executor = get_executor(pipeline.provider)
    executor.validate(pipeline)
    executor.run(pipeline)

if __name__ == "__main__":
    print("Comandos registrados:", app.registered_commands)
    app()
