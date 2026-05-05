import random
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image, ImageDraw, ImageFont


AVATAR_COLORS = [
    "#A8DADC",
    "#BDE0FE",
    "#CCD5AE",
    "#DDBEA9",
    "#CDB4DB",
]

TEXT_COLOR = "#2B2D42"


def generate_avatar(user):
    image = Image.new("RGB", (200, 200), random.choice(AVATAR_COLORS))
    draw = ImageDraw.Draw(image)

    letter = (user.name or "U")[0].upper()

    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            90
        )
    except OSError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), letter, font=font)
    x = (200 - (bbox[2] - bbox[0])) / 2
    y = (200 - (bbox[3] - bbox[1])) / 2

    draw.text((x, y), letter, fill=TEXT_COLOR, font=font)

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    return ContentFile(buffer.read(), name=f"{user.email}_avatar.png")