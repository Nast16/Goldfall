import json
import os

SAVE_PATH = "data/players.json"

DEFAULT_PLAYER = {
    "gold": 0,
    "inventory": {}
}

def load_player():
    if not os.path.exists(SAVE_PATH):
        return DEFAULT_PLAYER.copy()
    try:
        with open (SAVE_PATH, "r") as f:
            data = f.read().strip()

            if not data:
                return DEFAULT_PLAYER.copy()
            
            return json.loads(data)
    
    except json.JSONDecodeError:
        print("Save file corrupt. Creating new save.")
        return DEFAULT_PLAYER.copy()

def save_player(player_data):
    with open(SAVE_PATH, "w") as f:
        json.dump(player_data, f, indent=4)