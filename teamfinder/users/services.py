import random
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image, ImageDraw, ImageFont

from .constants import (
    AVATAR_COLORS,
    AVATAR_FONT_PATHS,
    AVATAR_FONT_SIZE,
    AVATAR_SIZE,
    AVATAR_TEXT_COLOR,
    TEXT_BBOX_ANCHOR,
)


def get_avatar_font():
    for font_path in AVATAR_FONT_PATHS:
        try:
            return ImageFont.truetype(
                font_path,
                AVATAR_FONT_SIZE,
            )
        except OSError:
            continue

    return ImageFont.load_default()


def generate_avatar(user):
    image = Image.new(
        "RGB",
        AVATAR_SIZE,
        random.choice(AVATAR_COLORS),
    )
    draw = ImageDraw.Draw(image)

    letter = (user.name or "U")[0].upper()
    font = get_avatar_font()

    bbox = draw.textbbox(
        TEXT_BBOX_ANCHOR,
        letter,
        font=font,
    )

    x = (AVATAR_SIZE[0] - (bbox[2] - bbox[0])) / 2
    y = (AVATAR_SIZE[1] - (bbox[3] - bbox[1])) / 2

    draw.text(
        (x, y),
        letter,
        fill=AVATAR_TEXT_COLOR,
        font=font,
    )

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    return ContentFile(
        buffer.read(),
        name=f"{user.email}_avatar.png",
    )
