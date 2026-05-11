from enum import StrEnum

USER_NAME_MAX_LENGTH = 124
USER_SURNAME_MAX_LENGTH = 124
USER_PHONE_MAX_LENGTH = 12
USER_ABOUT_MAX_LENGTH = 256

AVATAR_UPLOAD_PATH = "avatars/"
USERS_PER_PAGE = 12

GIT_HOST = "github.com"

INVALID_GIT_URL_MESSAGE = "Только Github"
INVALID_PHONE_MESSAGE = "Неверный формат номера телефона (пример: +79991111111)"

PHONE_REGEX = r"^(\+7|8)\d{10}$"


class AvatarColors(StrEnum):
    BLUE = "#A8DADC"
    LIGHT_BLUE = "#BDE0FE"
    GREEN = "#CCD5AE"
    BEIGE = "#DDBEA9"
    PURPLE = "#CDB4DB"


AVATAR_COLORS = [
    AvatarColors.BLUE,
    AvatarColors.LIGHT_BLUE,
    AvatarColors.GREEN,
    AvatarColors.BEIGE,
    AvatarColors.PURPLE,
]

AVATAR_SIZE = (200, 200)
AVATAR_TEXT_COLOR = "#2B2D42"

AVATAR_FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "arial.ttf",
]

AVATAR_FONT_SIZE = 90
TEXT_BBOX_ANCHOR = (0, 0)
