from engine.market import load_market, update_market, save_market
from engine.player import get_inventory, add_gold

def sell(item):
    market = load_market()
    inv = get_inventory()

    if item not in inv or inv[item] <= 0:
        print("Item tidak ada.")
        return
    
    if item not in market:
        print("Market tidak membeli item itu.")
        return
    
    price = market[item]["price"]

    inv[item] -= 1
    add_gold(price)

    market[item]["supply"] += 1
    save_market(market)

    print(f"Kamu menjual 1 {item} seharga {price} gold.")

    update_market()

