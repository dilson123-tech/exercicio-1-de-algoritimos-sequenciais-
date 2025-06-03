from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import openai
import os

# Carregar as variáveis do .env
load_dotenv()
print("CHAVE:", os.getenv("OPENAI_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Liberar o frontend para acessar a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, usar apenas o domínio certo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/perguntar")
async def perguntar(req: Request):
    data = await req.json()
    mensagem = data.get("mensagem")

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Pode trocar por "gpt-4" se tiver acesso
            messages=[
                {"role": "user", "content": mensagem}
            ]
        )
        return {"resposta": resposta.choices[0].message["content"]}
    except Exception as e:
        return {"erro": str(e)}
