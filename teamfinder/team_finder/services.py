import random
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image, ImageDraw, ImageFont


def generate_avatar(user):
    if user.avatar:
        return

    colors = ["#A8DADC", "#BDE0FE", "#CCD5AE", "#DDBEA9", "#CDB4DB"]

    image = Image.new("RGB", (200, 200), random.choice(colors))
    draw = ImageDraw.Draw(image)

    letter = user.name[0].upper()

    try:
        font = ImageFont.truetype("arial.ttf", 100)
    except OSError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), letter, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    draw.text(((200 - w) / 2, (200 - h) / 2), letter, fill="white", font=font)

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    user.avatar.save(
        f"{user.email}_avatar.png",
        ContentFile(buffer.getvalue()),
        save=False,
    )