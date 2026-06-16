import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_prompt():

    with open(
        "output/fact.json",
        "r",
        encoding="utf-8"
    ) as f:

        fact_data = json.load(f)

    fact = fact_data["fact"]

    prompt = f"""
Create image prompt.

Fact:
{fact}

Style:
Dark psychology page
Professional
Human subject
Instagram reel
Vertical 9:16
"""

    response = model.generate_content(prompt)

    image_prompt = response.text

    with open(
        "output/image_prompt.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(image_prompt)

    return image_prompt