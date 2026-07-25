import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENROUTER_API_KEY")
print("API KEY:", key)

client = OpenAI(
    api_key=key,
    base_url="https://openrouter.ai/api/v1"
)
MODEL = "openrouter/auto"

def generate_answer(question, chunks):

    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is not found, reply exactly:

"I could not find the answer in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content