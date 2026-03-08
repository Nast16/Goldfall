import random
from engine.market import load_market, save_market

EVENT_CHANCE = 0.1

def trigger_event():
    if random.random() > EVENT_CHANCE:
        return
    
    market = load_market()

    event = random.choice([
        "Forest_boom",
        "mine_collapse",
        "stone_shortage"
    ])

    print("\n WORLD EVENT!")

    if event == "forest_boom":
        print("Forest boom! Wood supply meningkat.")
        market["wood"]["price"] = max(1, market["wood"]["price"] - 3)

    elif event == "mine_collapse":
        print("Mine collapse! Iron jadi langka.")
        market["iron"]["price"] += 6
    
    elif event == "stone_shortage":
        print("Stone shortage di kota.")
        market["stone"]["price"] += 4
    
    save_market(market)