from godml.core.base_model_interface import BaseModel

class DummyModel(BaseModel):
    def train(self, X_train, y_train, X_test, y_test, params):
        return "model", [0, 1]
    
    def predict(self, model, X):
        return [1, 0]

def test_model_interface():
    model = DummyModel()
    assert isinstance(model, BaseModel)
