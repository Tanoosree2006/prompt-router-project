from groq import Groq
import os
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPTS

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def route_and_respond(message, intent):

    label = intent["intent"]

    if label == "unclear":
        return "Could you clarify what you need help with?"

    system_prompt = SYSTEM_PROMPTS[label]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":message}
        ]
    )

    return response.choices[0].message.content