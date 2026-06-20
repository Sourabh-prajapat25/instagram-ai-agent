from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json
import textwrap


def create_post():

    image = Image.open(
        "output/images/background.png"
    )

    image = image.resize((1080, 1920))

    image = image.convert("RGBA")

    draw = ImageDraw.Draw(image)

    with open(
        "output/content.json",
        "r",
        encoding="utf-8"
    ) as f:

        fact = json.load(f)["fact"]

    try:

        FONT_PATH = "assets/fonts/Montserrat-Bold.ttf"

        quote_font = ImageFont.truetype(
            FONT_PATH,
            77
        )

    except Exception as e:

        print("Font Error:", e)

        quote_font = ImageFont.load_default()

    wrapped = "\n".join(
        textwrap.wrap(
            fact,
            width=22
        )
    )

    bbox = draw.multiline_textbbox(
        (0, 0),
        wrapped,
        font=quote_font,
        spacing=20
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (1080 - text_width) // 2

    y = (1920 - text_height) // 2 - 450

    draw.multiline_text(
        (x, y),
        wrapped,
        fill="blue",
        font=quote_font,
        align="center",
        spacing=20
    )

    image = image.convert("RGB")

    image.save(
        "output/images/final_post.png",
        quality=95
    )

    print("✅ Post Created")
