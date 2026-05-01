import json
import os

FILE = "settings.json"

DEFAULT = {
    "snake_color": [0, 255, 0],
    "grid": True,
    "sound": True
}

def load_settings():
    if not os.path.exists(FILE):
        save_settings(DEFAULT)
        return DEFAULT
    with open(FILE, "r") as f:
        return json.load(f)

def save_settings(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)