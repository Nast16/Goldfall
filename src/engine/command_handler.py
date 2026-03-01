from system.gathering import gather
from engine.player import get_inventory
from engine.market import show_market
from system.trade import sell

def handle_command(cmd):
    if cmd == "gather":
        gather()

    elif cmd == "inventory":
        inv = get_inventory()

        print("=== INVENTORY ===")
        if not inv:
            print("Kosong.")
        else:
            for item, amt in inv.items():
                print(F"{item}: {amt}")

    elif cmd == "market":
        show_market()

    elif cmd.startswith("sell "):
        item = cmd.split(" ")[1]
        sell(item)

    elif cmd == "exit":
        exit()

    else:
        print("Unknown command")