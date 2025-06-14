# CNPJ Lookup Automation with n8n

This project is a workflow built with [n8n](https://n8n.io/) that automates the consultation of Brazilian CNPJ (business registry numbers) using the public API: [https://publica.cnpj.ws](https://publica.cnpj.ws).

## 🚀 Features

- Receives POST requests with a CNPJ number
- Queries the public CNPJ API
- Validates the response data
- Returns the company's legal name (`razao_social`), CNPJ and state (`UF`)
- Handles errors when the CNPJ is not found or invalid

## 📂 Workflow Structure

1. **Webhook Trigger** (`/webhook/consulta-cnpj-dilsbot`)
2. **HTTP Request** to external API
3. **IF Node** to validate if the response contains a valid company
4. **SET Node** to prepare success or error response
5. **Respond to Webhook** with the proper data

## 🧪 Sample Request (POST)

```json
POST /webhook/consulta-cnpj-dilsbot
Content-Type: application/json

{
  "cnpj": "19131243000197"
}
{
  "razao": "OPEN KNOWLEDGE BRASIL",
  "cnpj": "19131243000197",
  "uf": "SP"
}
 Use Case
This project simulates a real business automation scenario where a consulting firm or financial service integrates an external API to validate client information before onboarding.

👨‍💻 Author
Dilson Pereira — GitHub
Project guided by ProfessorDilsBot AI
