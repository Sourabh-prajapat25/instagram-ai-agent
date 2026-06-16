import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_content():

    prompt = """
Generate ONE viral psychology Instagram reel.

Return ONLY valid JSON.

{
    "fact":"",
    "source":"",
    "script":"",
    "caption":"",
    "image_prompts":[
        "",
        "",
        "",
        "",
        "",
        ""
    ]
}

Requirements:

- Fact must be psychology based
- Fact must come under 9-10 words
- Research backed
- Relationship topics preferred
- Man,boy or women,girls topics prefered
- fact words language is simple easy to understand
- Human behaviour topics preferred
- Script 100-120 words
- Caption engaging
- Include CTA
- Add 10 - 15 relevant hashtags at the end of caption 
- 6 cinematic image prompts
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    data = json.loads(text)

    # Save full content
    with open(
        "output/content.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    # Save fact separately
    with open(
        "output/fact.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "fact": data["fact"],
                "source": data["source"]
            },
            f,
            indent=4,
            ensure_ascii=False
        )

    print("✅ New content generated")
    print("Fact:", data["fact"])

    return data