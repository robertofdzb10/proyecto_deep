# models/gpt4_integration.py
import openai
from config import API_KEY_GPT4O

# Configura la API key de GPT-4o
openai.api_key = API_KEY_GPT4O

class GPT4Integration:
    """
    Integra GPT-4o para refinar respuestas y extraer información con máxima claridad,
    actuando como un experto en cada tarea.
    """

    def __init__(self):
        # Puedes agregar parámetros de configuración adicionales si es necesario
        pass

    def refinar_respuesta(self, user_input: str, prediction: str) -> str:
        """
        Llama a GPT-4o para refinar y mejorar la respuesta combinando el input del usuario y la predicción,
        actuando como un experto en comunicación profesional.
        
        Args:
            user_input (str): Texto original del usuario.
            prediction (str): Resultado de la predicción.
        
        Returns:
            str: Respuesta final refinada y profesional.
        """
        prompt = (
            "Eres un experto en comunicación profesional y en redacción clara y precisa. "
            "Tu tarea es combinar la siguiente información de manera coherente y atractiva:\n\n"
            f"Información del usuario: \"{user_input}\"\n"
            f"Resultado de la predicción: \"{prediction}\"\n\n"
            "Genera una respuesta final que sea extremadamente clara, profesional y empática, "
            "informando al usuario del resultado de forma precisa y sin ambigüedades."
            "Limita tu respuesta a un máximo de 150 tokens."
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=150,
            )
            refined = response.choices[0].message.content.strip()
            return refined
        except Exception as e:
            return f"La predicción es: {prediction} (No se pudo refinar la respuesta: {e})"

    def extract_teams(self, text: str) -> tuple:
        """
        Utiliza GPT-4o para extraer con precisión los nombres de los dos equipos de fútbol del texto,
        actuando como un experto en reconocimiento de entidades y extracción de información.
        
        Args:
            text (str): Texto de entrada que puede contener nombres de equipos, incluso en contextos complejos.
        
        Returns:
            tuple: Una tupla con dos nombres de equipos, o None si no se pudieron extraer.
        """
        prompt = (
            "Eres un experto en extracción de entidades y reconocimiento de nombres en textos complejos, "
            "especializado en identificar nombres de equipos de fútbol. "
            "Tu tarea es analizar el siguiente texto y extraer con máxima precisión los nombres de los dos equipos "
            "de fútbol mencionados, sin incluir información adicional. "
            "Devuelve únicamente los dos nombres en el siguiente formato: \"Equipo1, Equipo2\".\n\n"
            f"Texto: \"{text}\""
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=50,
            )
            result = response.choices[0].message.content.strip()
            # Se espera un resultado en el formato "Equipo1, Equipo2"
            teams = [team.strip() for team in result.split(",") if team.strip()]
            if len(teams) >= 2:
                return teams[0], teams[1]
            else:
                return None
        except Exception as e:
            print(f"Error al extraer equipos: {e}")
            return None
