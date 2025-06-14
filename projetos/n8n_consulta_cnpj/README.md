# Consulta de CNPJ via N8N

Este projeto implementa um fluxo no N8N para consultar dados de CNPJ usando a API pública do [https://publica.cnpj.ws](https://publica.cnpj.ws).

## 🧠 Objetivo

Permitir que qualquer sistema (ou usuário) envie um CNPJ via webhook e receba como resposta os dados básicos da empresa consultada.

## 🚀 Tecnologias

- N8N
- Webhook
- HTTP Request
- API Pública do CNPJ
- Lógica condicional (`IF`)
- Manipulação de dados (`Set`)
- Retorno customizado (`Respond to Webhook`)

## 📦 Estrutura

```bash
n8n_consulta_cnpj/
├── workflow.json
├── README.md
📌 Como usar
Importe o workflow.json no N8N (via "Import workflow").

Ative o fluxo (modo Production).

Envie uma requisição POST para o endpoint:

bash
Copiar código
POST /webhook/consulta-cnpj-dilsbot
Content-Type: application/json

{
  "cnpj": "19131243000197"
}
✅ Exemplo de resposta
json
Copiar código
{
  "razao": "OPEN KNOWLEDGE BRASIL",
  "cnpj": "19131243000197",
  "uf": "SP"
}
❌ Erro esperado
json
Copiar código
{
  "erro": "CNPJ inválido ou não encontrado."
}
📘 Observação
Este projeto foi desenvolvido por Dilson (@dilson123-tech) como parte dos estudos de integração entre automações e APIs públicas usando N8N.
