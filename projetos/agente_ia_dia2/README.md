# 🤖 ProfessorDilsBot - Agente IA com FastAPI

Este é um projeto de agente inteligente construído em Python com FastAPI, integrado à OpenAI API (GPT-4).  
Faz parte do **Desafio 7 Dias de IA** do Dilson, programador e visionário brasileiro. 🇧🇷💻

---

## 🚀 Tecnologias

- Python 3.10+
- FastAPI
- OpenAI API (GPT-4 ou GPT-3.5)
- dotenv
- Uvicorn
- Swagger UI (auto gerado em `/docs`)

---

## 📁 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/SEU-USUARIO/agente_ia_dia2.git

# Vá até a pasta
cd agente_ia_dia2

# Instale as dependências
pip install -r requirements.txt

# Crie o arquivo .env com sua chave:
echo "OPENAI_API_KEY=sua-chave-aqui" > .env

# Rode o servidor local
uvicorn fastapi_app:app --reload

Acesse: http://127.0.0.1:8000/docs

💬 Como funciona
O prompt base está em prompt_base.txt

O endpoint /perguntar recebe uma pergunta e retorna a resposta do ProfessorDilsBot

O modelo usado é gpt-4, mas pode ser alterado para gpt-3.5-turbo para economizar tokens

🧠 Créditos
Projeto feito por Dilson Pereira com auxílio do ProfessorDilsBot.
Faz parte do plano de especialização em IA e Programação com foco em projetos reais.


yaml
Copiar
Editar

---

