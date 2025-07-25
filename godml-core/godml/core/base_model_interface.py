from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def train(self, X_train, y_train, X_test, y_test, params):
        """
        Entrena el modelo y devuelve dos objetos:
        - model: objeto entrenado (serializable)
        - preds: predicciones sobre X_test
        """
        pass

    @abstractmethod
    def predict(self, model, X):
        """
        Realiza inferencias sobre un conjunto de datos X.
        Retorna las predicciones.
        """
        pass
