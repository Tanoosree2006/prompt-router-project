import json
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_intent(message):

    prompt = f"""
Classify the user's intent.

Possible intents:
code
data
writing
career
unclear

Return ONLY JSON like:
{{"intent":"label","confidence":0.0}}

User message:
{message}
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role":"user","content":prompt}]
        )

        result = json.loads(response.choices[0].message.content)

        return result

    except:

        return {"intent":"unclear","confidence":0.0}