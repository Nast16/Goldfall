from engine.save_system import load_player, save_player

player = load_player()


def get_gold():
    return player["gold"]

def add_gold(amount):
    player["gold"] += amount
    save_player(player)

def add_item(item, amount):
    inv = player["inventory"]

    if item not in inv:
        inv[item] = 0
    
    inv[item] += amount
    save_player(player)

def get_inventory():
    return player["inventory"]