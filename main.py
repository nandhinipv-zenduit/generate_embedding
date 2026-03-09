import os
import json
import openai
import requests

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
ticket_id = os.getenv("TICKET_ID")
ticket_subject = os.getenv("TICKET_SUBJECT")
ticket_description = os.getenv("TICKET_DESCRIPTION")
zoho_webhook_url = os.getenv("ZOHO_FLOW_WEBHOOK")

# Validate inputs
if not ticket_subject:
    raise ValueError("TICKET_SUBJECT is required")
if not ticket_description:
    raise ValueError("TICKET_DESCRIPTION is required")
if not ticket_id:
    raise ValueError("TICKET_ID is required")
if not zoho_webhook_url:
    raise ValueError("ZOHO_FLOW_WEBHOOK is required")

# Generate embedding
try:
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=f"{ticket_subject}\n{ticket_description}"
    )
    embedding_vector = response['data'][0]['embedding']
except Exception as e:
    print("Error generating embedding:", e)
    embedding_vector = []

# Prepare payload for Zoho Flow
payload = {
    "ticket_id": ticket_id,
    "ticket_subject": ticket_subject,
    "ticket_description": ticket_description,
    "embedding": embedding_vector
}

# Send to Zoho Flow webhook
try:
    headers = {"Content-Type": "application/json"}
    res = requests.post(zoho_webhook_url, headers=headers, data=json.dumps(payload))
    print("Webhook response:", res.status_code, res.text)
except Exception as e:
    print("Error sending to Zoho Flow:", e)
