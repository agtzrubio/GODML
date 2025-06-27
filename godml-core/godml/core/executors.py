from godml.providers.mlflow import MLflowExecutor
from godml.providers.sagemaker import SageMakerExecutor

_providers_map = {
    "mlflow": MLflowExecutor,
    "sagemaker": SageMakerExecutor,
}

def get_executor(provider_name: str):
    provider = provider_name.lower()

    if provider == "mlflow":
        from godml.providers.mlflow import MLflowExecutor
        return MLflowExecutor()
    elif provider == "sagemaker":
        from godml.providers.sagemaker import SageMakerExecutor
        return SageMakerExecutor()
    else:
        raise ValueError(f"Provider '{provider_name}' no soportado.")
