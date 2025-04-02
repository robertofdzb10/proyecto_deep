# services/prediction_model.py

import random

class PredictionModel:
    """
    Clase de predicción que define la interfaz para obtener resultados de partidos.
    Actualmente, simula la predicción devolviendo un resultado aleatorio.
    En el futuro, se implementará la lógica real del modelo sin cambiar la interfaz.
    """
    
    def __init__(self):
        self.possible_results = ["2-1", "1-0", "0-0", "3-2", "1-1"]

    def predict(self, user_input: str) -> str:
        """
        Simula una predicción basada en el input del usuario.

        Args:
            user_input (str): Texto del usuario (por ejemplo, con información del partido).

        Returns:
            str: Resultado simulado del partido.
        """
        # Aquí se puede agregar lógica basada en el contenido de user_input,
        # pero por ahora se retorna un resultado aleatorio.
        return random.choice(self.possible_results)
