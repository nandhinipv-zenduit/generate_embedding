# main.py
import os
from openai import OpenAI

# Read environment variables from GitHub Actions
TICKET_ID = os.getenv("TICKET_ID")
TICKET_SUBJECT = os.getenv("TICKET_SUBJECT")
TICKET_DESCRIPTION = os.getenv("TICKET_DESCRIPTION")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Simple validation
if not TICKET_ID:
    raise ValueError("TICKET_ID is required")
if not TICKET_SUBJECT:
    raise ValueError("TICKET_SUBJECT is required")
if not TICKET_DESCRIPTION:
    raise ValueError("TICKET_DESCRIPTION is required")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is required")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

try:
    # Generate embedding using the "small" model
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=f"{TICKET_SUBJECT}\n{TICKET_DESCRIPTION}"
    )

    embedding_vector = response.data[0].embedding

    print(f"Ticket ID: {TICKET_ID}")
    print(f"Embedding length: {len(embedding_vector)}")
    print(f"Embedding preview (first 10 values): {embedding_vector[:10]}")

except Exception as e:
    print("Error generating embedding:", e)
    raise
