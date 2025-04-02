# api/prediction_api.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.deep_agent import DeepAgent

app = FastAPI()

# Configurar CORS para permitir solicitudes de cualquier origen (ajusta según sea necesario)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Puedes restringir esto a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = DeepAgent()

class PredictionRequest(BaseModel):
    user_input: str

@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        respuesta = agent.procesar_input(request.user_input)
        return {"prediction": respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
