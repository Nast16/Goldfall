import json
import random

MARKET_PATH = "data/market.json"


def load_market():
    with open(MARKET_PATH, "r") as f:
        return json.load(f)
    
def save_market(data):
    with open(MARKET_PATH, "w") as f:
        json.dump(data, f, indent=4)

def update_market():
    market = load_market()

    for item, info in market.items():

        random_change = random.randint(
            -info["volatility"], info["volatility"]
        )

        supply_effect = -(info["supply"] // 3)

        info["price"] += random_change + supply_effect
        
        info["price"] = max(1, info["price"])

        info["supply"] = max(0, info["supply"] - 1)

    save_market(market)

def show_market():
    market = load_market()

    print("=== MARKET ===")
    for item, info in market.items():
        print(f"{item}: {info['price']} gold")