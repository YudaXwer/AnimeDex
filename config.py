# Your TechZ Api Key
# Get from @TechZApiBot on Telegram | https://t.me/TechZApiBot

from os import getenv


API_KEY = "RZOCAY"

if not API_KEY or API_KEY == "RZOCAY" or API_KEY == "RZOCAY":
    API_KEY = getenv("API_KEY")

    if not API_KEY:
        raise Exception("Please add your TechZ Api Key in config.py file")
