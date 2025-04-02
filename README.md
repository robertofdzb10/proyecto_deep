# Proyecto Deep

**Proyecto Deep** es una aplicación de predicción deportiva que utiliza técnicas avanzadas de deep learning y procesamiento de lenguaje natural para ofrecer predicciones sobre resultados de partidos de fútbol. La arquitectura está diseñada para ser modular, escalable y fácilmente mantenible, permitiendo la integración de un modelo real de predicción en el futuro sin modificar la interfaz de comunicación.

---

## Índice

- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Arquitectura y Flujo de Datos](#arquitectura-y-flujo-de-datos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Uso y Ejecución](#uso-y-ejecución)
- [API](#api)
- [Frontend](#frontend)
- [Entrenamiento y Evaluación del Modelo](#entrenamiento-y-evaluación-del-modelo)
- [Utilidades](#utilidades)
- [Notas Adicionales](#notas-adicionales)

---

## Características

- **Interfaz de Chat:** Una interfaz web minimalista y profesional que permite a los usuarios enviar consultas y recibir predicciones en un formato de chat.
- **API REST:** Construida con FastAPI, expone un endpoint para recibir las solicitudes de predicción y retornar las respuestas procesadas.
- **Agente de Predicción:** Un módulo central que procesa el input del usuario, extrae información relevante y coordina la llamada al modelo de predicción.
- **Modelo de Deep Learning:** Una arquitectura definida y entrenada para realizar predicciones de resultados deportivos. La implementación del modelo se encuentra en `models/model.py` y su entrenamiento en `models/train_evaluate.py`.
- **Integración con GPT-4:** Un módulo de integración (`models/gpt4_integration.py`) que se utiliza para refinar las respuestas y extraer entidades relevantes (por ejemplo, nombres de equipos) de textos complejos.
- **Modularidad y Separación de Responsabilidades:** La estructura del proyecto permite que cada componente se desarrolle y se mantenga de manera independiente.

---

## Estructura del Proyecto

La siguiente es la estructura completa del proyecto:

```plaintext
PROYECTO_DEEP/
├── __pycache__/
├── agents/
│   ├── __pycache__/
│   └── deep_agent.py           # Agente central que procesa el input, coordina la predicción y refina la respuesta
├── api/
│   ├── __pycache__/
│   └── prediction_api.py       # Endpoint de FastAPI que expone la funcionalidad de predicción
├── data/
│   ├── processed/              # Datos preprocesados para el entrenamiento del modelo
│   └── raw/                    # Datos sin procesar (históricos, CSV, etc.)
├── frontend/
│   ├── css/
│   │   └── styles.css          # Estilos de la interfaz web
│   ├── js/                     # Lógica JavaScript para interactuar con la API
│   └── index.html              # Interfaz principal tipo chat
├── models/
│   ├── __pycache__/
│   ├── gpt4_integration.py     # Integración con GPT-4 para refinar respuestas y extraer información
│   ├── model.py                # Definición de la arquitectura del modelo de deep learning
│   ├── prediction_model.py     # Clase que actúa como interfaz para obtener predicciones (llama al modelo real)
│   └── train_evaluate.py       # Script para entrenar y evaluar el modelo de predicción
├── utils/
│   └── data_preprocessing.py   # Funciones para la limpieza y transformación de datos
├── venv/                       # Entorno virtual (no incluido en el repositorio)
├── .gitignore                  # Archivos y carpetas a ignorar por Git
├── config.py                   # Configuración global (rutas, API keys, etc.)
└── requirements.txt            # Dependencias del proyecto
```

---

## Arquitectura y Flujo de Datos

El flujo de datos de la aplicación es el siguiente:

1. **Frontend (Interfaz de Chat):**  
   - El usuario ingresa su consulta a través de una interfaz web minimalista.
   - El frontend envía una solicitud HTTP POST al endpoint `/predict` de la API.

2. **API (FastAPI):**  
   - El endpoint recibe la solicitud y la envía al agente de predicción.
   - Se gestiona el CORS para permitir el acceso desde la interfaz web.

3. **Agente (DeepAgent):**  
   - Procesa el input del usuario.
   - Utiliza el módulo de integración con GPT-4 para extraer información relevante (por ejemplo, nombres de equipos).
   - Llama a la función `obtener_prediccion` para obtener la predicción del resultado del partido.
   - Refina la respuesta combinando el input del usuario con la predicción mediante GPT-4.

4. **Modelo de Predicción:**  
   - La clase `PredictionModel` en `models/prediction_model.py` define la interfaz para obtener una predicción.
   - La implementación real del modelo (definida en `models/model.py` y entrenada mediante `models/train_evaluate.py`) se invocará a través de esta interfaz.

5. **Respuesta:**  
   - La API retorna la respuesta refinada al frontend.
   - La interfaz muestra el resultado al usuario en formato de chat.

---

## Instalación y Configuración

### Requisitos

- Python 3.7 o superior
- Entorno virtual (recomendado)

### Instalación

1. Clona el repositorio:

   ```bash
   git clone https://tu-repositorio.git
   cd PROYECTO_DEEP
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en el archivo `.env` (crea el archivo en la raíz del proyecto):

   ```dotenv
   API_KEY_GPT4O=tu_api_key_aqui
   MODEL_PATH=models/model.h5
   DATA_RAW_PATH=data/raw/
   DATA_PROCESSED_PATH=data/processed/
   ```

5. Asegúrate de que el archivo `config.py` carga correctamente las variables del archivo `.env`.

---

## Uso y Ejecución

### Ejecutar la API

Para iniciar la API de FastAPI, ejecuta:

```bash
python -m uvicorn api.prediction_api:app --reload
```

La API se iniciará en `http://127.0.0.1:8000`.

### Ejecutar el Frontend

1. Abre el archivo `frontend/index.html` en tu navegador.
2. Interactúa con el chat: escribe tu consulta y presiona "Enviar".
3. La interfaz enviará la solicitud a la API y mostrará la respuesta del agente.

---

## API

### Endpoint: `/predict`

- **Método:** `POST`
- **Descripción:** Recibe una consulta del usuario y retorna una predicción refinada.
- **Cuerpo de la Solicitud (JSON):**

  ```json
  {
    "user_input": "Texto de la consulta del usuario"
  }
  ```

- **Respuesta (JSON):**

  ```json
  {
    "prediction": "Respuesta refinada con la predicción"
  }
  ```

---

## Frontend

La carpeta `frontend/` contiene:

- **index.html:** La interfaz principal tipo chat.
- **css/styles.css:** Estilos para una apariencia moderna y profesional.
- **js/app.js:** Lógica en JavaScript para enviar solicitudes a la API y mostrar las respuestas en el chat.

---

## Entrenamiento y Evaluación del Modelo

La carpeta `models/` incluye:

- **model.py:** Define la arquitectura real del modelo de deep learning.
- **train_evaluate.py:** Script para entrenar y evaluar el modelo utilizando los datos preprocesados.
- **prediction_model.py:** Clase que actúa como interfaz para obtener predicciones; en la versión final, llamará al modelo real entrenado.
- **gpt4_integration.py:** Módulo para integrar GPT-4, que refina las respuestas y extrae entidades relevantes.

---

## Utilidades

La carpeta `utils/` contiene scripts para:

- **data_preprocessing.py:** Funciones para limpiar y transformar los datos históricos, preparándolos para el entrenamiento del modelo.

---

## Notas Adicionales

- **Modularidad:** La separación en carpetas permite que cada componente (agente, API, modelo, frontend) se desarrolle y se mantenga de forma independiente.
- **Interfaz Unificada:** La clase `PredictionModel` en `models/prediction_model.py` ofrece una interfaz única para obtener predicciones, de modo que el resto del sistema no necesita conocer la implementación interna del modelo.
- **Integración con GPT-4:** Se utiliza GPT-4 para refinar respuestas y extraer información relevante, mejorando la interacción y la precisión de las respuestas.
- **Escalabilidad:** La arquitectura está diseñada para facilitar la integración de un modelo real de deep learning sin necesidad de reestructurar el código existente.

---