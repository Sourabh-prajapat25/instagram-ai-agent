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
Generate ONE viral Instagram riddle reel.

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

- fact field must contain the riddle text
- Riddle must be short under (15 - 20 words)
- Give Riddle that not has high vocabulary
- you can Enter the sentence also for good looking it increace readbility 
- Very easy English
- Easy to understand
- Funny, tricky or brain teaser style
- Must encourage people to think
- No answer in fact field
- No emojis in fact field
- Maximum 2 short lines
- source field should contain:
  "Generated Riddle"

- script must be 80-120 words
- Script should talk about the riddle and encourage viewers to think before checking comments
- Do NOT reveal the answer in the script

- Caption must be engaging
- Ask users to comment their answer
- Include CTA:
  "Comment your answer below 👇"

- Add 10-15 relevant riddle hashtags at the end of caption


Examples of good riddles:

What has many keys
but can't open a door?

Boys wear it daily, but
girls wear it once a year
what is it ?

I go up
but never come down.
What am I?

Output ONLY valid JSON.
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
