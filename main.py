import os
import openai

# Read environment variables
TICKET_ID = os.getenv("TICKET_ID")
TICKET_SUBJECT = os.getenv("TICKET_SUBJECT")
TICKET_DESCRIPTION = os.getenv("TICKET_DESCRIPTION")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate required fields
if not TICKET_ID:
    raise ValueError("TICKET_ID is required")
if not TICKET_SUBJECT:
    raise ValueError("TICKET_SUBJECT is required")
if not TICKET_DESCRIPTION:
    raise ValueError("TICKET_DESCRIPTION is required")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is required")

# Combine subject + description for embedding
text_to_embed = f"{TICKET_SUBJECT}\n{TICKET_DESCRIPTION}"

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY

# Generate embedding
try:
    response = openai.Embedding.create(
        input=text_to_embed,
        model="text-embedding-3-large"
    )
    embedding = response['data'][0]['embedding']
    print(f"Embedding generated for ticket {TICKET_ID}:")
    print(embedding[:10], "...")  # Print first 10 numbers as sample
except Exception as e:
    print(f"Error generating embedding: {e}")
