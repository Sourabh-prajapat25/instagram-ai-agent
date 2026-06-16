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

        quote_font = ImageFont.truetype(
            "arial.ttf",
            95
        )

        cta_font = ImageFont.truetype(
            "arial.ttf",
            48
        )

        brand_font = ImageFont.truetype(
            "arial.ttf",
            42
        )

    except:

        quote_font = ImageFont.load_default()
        cta_font = ImageFont.load_default()
        brand_font = ImageFont.load_default()

    wrapped = "\n".join(
        textwrap.wrap(
            fact,
            width=22
        )
    )

    # Quote box size
    bbox = draw.multiline_textbbox(
        (0, 0),
        wrapped,
        font=quote_font,
        spacing=20
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center quote
    x = (1080 - text_width) // 2
    y = (1920 - text_height) // 2 - 250

    draw.multiline_text(
        (x, y),
        wrapped,
        fill="white",
        font=quote_font,
        align="center",
        spacing=20
    )

    


    # Username
    draw.text(
        (300, 1600),
        "Follow @psychology_see",
        fill="yellow",
        font=brand_font
    )

    image = image.convert("RGB")

    image.save(
        "output/images/final_post.png",
        quality=95
    )

    print("✅ Post Created")