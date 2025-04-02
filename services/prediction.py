# services/prediction.py

from services.prediction_model import PredictionModel

def obtener_prediccion(user_input: str) -> str:
    """
    Función que encapsula la llamada a la clase PredictionModel.
    Actualmente utiliza la implementación simulada,
    pero en el futuro se podrá modificar la lógica interna sin cambiar la interfaz.

    Args:
        user_input (str): Texto del usuario.

    Returns:
        str: Resultado de la predicción (simulada por ahora).
    """
    model = PredictionModel()
    return model.predict(user_input)
