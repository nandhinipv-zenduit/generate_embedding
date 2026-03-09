import os
import json
import openai

# Get ticket info from environment variables
TICKET_ID = os.getenv("TICKET_ID")
TICKET_SUBJECT = os.getenv("TICKET_SUBJECT")
TICKET_DESCRIPTION = os.getenv("TICKET_DESCRIPTION")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Basic validation
if not TICKET_SUBJECT or not TICKET_DESCRIPTION:
    raise ValueError("TICKET_SUBJECT and TICKET_DESCRIPTION are required")

openai.api_key = OPENAI_API_KEY

try:
    # Generate embedding using the small model
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=TICKET_SUBJECT + "\n" + TICKET_DESCRIPTION
    )

    embedding = response['data'][0]['embedding']

    # Output to JSON (this can be picked up by GitHub or other apps)
    result = {
        "ticket_id": TICKET_ID,
        "embedding": embedding
    }

    # Save result to file
    with open("result.json", "w") as f:
        json.dump(result, f)

    print(json.dumps(result))  # So GitHub Actions logs show it

except Exception as e:
    print("Error generating embedding:", str(e))
    raise
