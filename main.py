import os
import json
import openai

# Load environment variables
TICKET_ID = os.environ.get("TICKET_ID")
TICKET_SUBJECT = os.environ.get("TICKET_SUBJECT")
TICKET_DESCRIPTION = os.environ.get("TICKET_DESCRIPTION")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Basic validation
if not TICKET_ID or not TICKET_SUBJECT or not TICKET_DESCRIPTION:
    raise ValueError("TICKET_ID, TICKET_SUBJECT and TICKET_DESCRIPTION are required")

openai.api_key = OPENAI_API_KEY

try:
    # Generate embedding using the small model
    response = openai.Embedding.create(
        input=TICKET_DESCRIPTION,
        model="text-embedding-3-small"
    )
    embedding = response['data'][0]['embedding']

    # Prepare JSON output for Zoho Flow
    output = {
        "ticket_id": TICKET_ID,
        "ticket_subject": TICKET_SUBJECT,
        "embedding": embedding
    }

    # Print JSON so GitHub Action captures it
    print(json.dumps(output))

except Exception as e:
    print(json.dumps({"error": str(e)}))
    raise
