#converts earth date to fictional date

from pathlib import Path

def get_config():
    path = Path("config") / "date_config.json"

    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def converter():
    pass