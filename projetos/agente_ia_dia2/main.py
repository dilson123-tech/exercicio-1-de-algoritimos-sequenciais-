import openai
import os
from dotenv import load_dotenv

# Carregar a chave da OpenAI do .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Carregar o prompt base
with open("prompt_base.txt", "r", encoding="utf-8") as f:
    prompt_base = f.read()

def conversar(comando_usuario):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # ou "gpt-3.5-turbo" se preferir
        messages=[
            {"role": "system", "content": prompt_base},
            {"role": "user", "content": comando_usuario}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

# Exemplo de uso
if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            break
        resposta = conversar(user_input)
        print("ProfessorDilsBot:", resposta)
