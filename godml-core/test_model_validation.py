from godml.core.base_model_interface import BaseModel

class MyModel(BaseModel):
    def train(self, X_train, y_train, X_test, y_test, params):
        return "modelo_entrenado", [0, 1]

    def predict(self, model, X):
        return [1, 0]

if __name__ == "__main__":
    model_instance = MyModel()

    if isinstance(model_instance, BaseModel):
        print("✅ MyModel implementa correctamente la interfaz BaseModel.")
    else:
        print("❌ MyModel NO implementa BaseModel.")
