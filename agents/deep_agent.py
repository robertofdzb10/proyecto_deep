# agents/deep_agent.py
from services.prediction import obtener_prediccion
from models.gpt4_integration import GPT4Integration

class DeepAgent:
    """
    Agente que procesa el input del usuario, extrae información y coordina la llamada a la API
    de predicción. Además, utiliza GPT-4o para refinar la respuesta y extraer con precisión los nombres
    de los equipos en contextos complejos.
    """

    def __init__(self):
        self.gpt4 = GPT4Integration()

    def procesar_input(self, user_input: str) -> str:
        """
        Procesa el input del usuario, extrae los nombres de los equipos y devuelve la respuesta refinada.
        
        Args:
            user_input (str): Mensaje del usuario.
        
        Returns:
            str: Respuesta final refinada del agente.
        """
        # Extraer equipos usando GPT-4o para mayor robustez en contextos variados
        teams = self._extract_teams(user_input)
        print(f"Equipos extraídos: {teams}")
        
        try:
            prediction = obtener_prediccion(user_input)
        except Exception as e:
            return f"Error al obtener la predicción: {e}"

        # Refinar la respuesta combinando el input y la predicción a través de GPT-4o
        response = self.gpt4.refinar_respuesta(user_input, prediction)
        return response

    def _extract_teams(self, text: str):
        """
        Extrae los nombres de los equipos utilizando GPT-4o.
        
        Args:
            text (str): Texto de entrada.
        
        Returns:
            tuple or None: Tupla con dos nombres de equipos, o None si no se detectan.
        """
        return self.gpt4.extract_teams(text)
