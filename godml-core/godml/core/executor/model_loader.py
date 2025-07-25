import os
import importlib.util
from godml.core.base_model_interface import BaseModel

def load_custom_model_class(project_path: str, model_type: str) -> BaseModel:
    """
    Carga dinámicamente un modelo desde 'models/{model_type}_model.py'
    """
    model_filename = f"{model_type}_model.py"
    model_file = os.path.join(project_path, "models", model_filename)

    if not os.path.isfile(model_file):
        raise FileNotFoundError(f"❌ No se encontró el modelo en: {model_file}")

    # Convención: nombre de clase en PascalCase
    class_name = ''.join([part.capitalize() for part in model_type.split('_')]) + "Model"

    # Cargar dinámicamente el archivo
    spec = importlib.util.spec_from_file_location(class_name, model_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Obtener la clase del modelo
    model_class = getattr(module, class_name)
    model_instance = model_class()

    if not isinstance(model_instance, BaseModel):
        raise TypeError(f"❌ {class_name} no implementa BaseModel correctamente.")

    return model_instance
