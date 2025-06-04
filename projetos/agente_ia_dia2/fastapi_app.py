from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Carregar chave da OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Carregar prompt base
with open("prompt_base.txt", "r", encoding="utf-8") as f:
    prompt_base = f.read()

# Modelo de dados esperado
class Mensagem(BaseModel):
    pergunta: str

# Inicializar app FastAPI
app = FastAPI()

# Liberar CORS (pra conectar com o frontend amanhã)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Rota principal da IA
@app.post("/perguntar")
def responder(mensagem: Mensagem):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Pode trocar por "gpt-3.5-turbo" se quiser
        messages=[
            {"role": "system", "content": prompt_base},
            {"role": "user", "content": mensagem.pergunta}
        ],
        temperature=0.7
    )
    resposta = response['choices'][0]['message']['content']
    return {"resposta": resposta}
