import os
import json
import requests
import openai

# Load env variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ZOHO_FLOW_WEBHOOK = os.getenv("ZOHO_FLOW_WEBHOOK")
TICKET_ID = os.getenv("TICKET_ID")
TICKET_SUBJECT = os.getenv("TICKET_SUBJECT")
TICKET_DESCRIPTION = os.getenv("TICKET_DESCRIPTION")

# Basic validation
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is required")
if not ZOHO_FLOW_WEBHOOK:
    raise ValueError("ZOHO_FLOW_WEBHOOK is required")
if not TICKET_ID:
    raise ValueError("TICKET_ID is required")
if not TICKET_SUBJECT:
    raise ValueError("TICKET_SUBJECT is required")
if not TICKET_DESCRIPTION:
    raise ValueError("TICKET_DESCRIPTION is required")

openai.api_key = OPENAI_API_KEY

try:
    # Generate embedding
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=f"{TICKET_SUBJECT}\n{TICKET_DESCRIPTION}"
    )
    embedding_vector = response["data"][0]["embedding"]

    # Prepare payload
    payload = {
        "ticket_id": TICKET_ID,
        "ticket_subject": TICKET_SUBJECT,
        "ticket_description": TICKET_DESCRIPTION,
        "embedding": embedding_vector
    }

    # Send back to Zoho Flow webhook
    headers = {"Content-Type": "application/json"}
    res = requests.post(ZOHO_FLOW_WEBHOOK, headers=headers, json=payload)
    res.raise_for_status()

    # Print response for debug
    print("Zoho Flow webhook response:", res.status_code, res.text)
    print(json.dumps(payload))

except Exception as e:
    print("Error:", e)
    raise
