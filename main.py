import os
import json
from openai import OpenAI

# Load environment variable for OpenAI API
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set in environment")

client = OpenAI(api_key=OPENAI_API_KEY)

# Inputs from Zoho Flow (or GitHub Action workflow dispatch)
TICKET_ID = os.getenv("TICKET_ID")
TICKET_SUBJECT = os.getenv("TICKET_SUBJECT")
TICKET_DESCRIPTION = os.getenv("TICKET_DESCRIPTION")

if not TICKET_SUBJECT or not TICKET_DESCRIPTION:
    raise ValueError("TICKET_SUBJECT and TICKET_DESCRIPTION are required")

# Generate embedding
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=ticket_summary
)

embedding_vector = response.data[0].embedding

# Output JSON (Zoho Flow can parse this)
output = {
    "ticket_id": ticket_id,
    "embedding": embedding_vector
}

# Print JSON to stdout
print(json.dumps(output))
