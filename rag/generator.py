import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_answer(question, chunks):

    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is not found, say:
"I could not find the answer in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text