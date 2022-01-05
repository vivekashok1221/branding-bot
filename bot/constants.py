import os
import pathlib
from typing import NamedTuple

from disnake import Colour

from bot.utils.env import env_list

ENVIRONMENT = os.getenv("ENVIRONMENT")
if ENVIRONMENT is None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=f"{os.getcwd()}/.env")

# Environment variables
PREFIX = os.getenv("PREFIX", "b!")
TOKEN = os.getenv("TOKEN")
INVITE = os.getenv("INVITE")
SERVER_INVITE = os.getenv("SERVER_INVITE")
DEBUG = os.getenv("DEBUG", False)
TEST_SERVERS = env_list(os.getenv("TEST_SERVERS"), type_=int)

# Paths
EXTENSIONS = pathlib.Path("bot/exts/")
LOG_FILE = pathlib.Path("log/gurkbot.log")

OUTPUT_IMAGE_FORMATS = [
    "PNG",
    "JPEG",
    "ICO",
    "GIF",
    "PDF",
    "WEBP",
]  # `image_to_file` depends on this being uppercase.


class About(NamedTuple):
    name = "Branding Bot"
    description = "A Discord utility bot for working with server branding."
    repo_url = "https://github.com/gustavwilliam/branding-bot"


# Embeds
class EmbedColors(NamedTuple):
    info = Colour.blurple()
    confirmation = Colour.green()
    warning = Colour.yellow()
    error = Colour.red()


class EmbedEmojis(NamedTuple):
    confirmation = "\u2705"
    warning = "\u26a0\ufe0f"
    error = "\u274c"


class EmbedTitles(NamedTuple):
    confirmation = [
        "Done!",
        "Alright",
        "Sure thing!",
        "You got it!",
        "Affirmative",
        "No problem!",
    ]
    warning = [
        "Be careful",
        "Proceed with caution",
        "Are you sure about that?",
    ]
    error = [
        "Nope",
        "Definitely not",
        "Let's not do that",
        "That was a mistake",
        "Out of the question",
        "That doesn't seem right",
    ]
