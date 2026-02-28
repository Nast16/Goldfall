import random
from engine.player import add_item

RESOURCES = {
    "wood": (1, 5),
    "iron": (0, 2),
    "stone": (1, 3)
}

def gather():
    print("Kamu pergi mengumpulkan resource...\n")

    for resource, (min_amt, max_amt) in RESOURCES.items():
        amount = random.randint(min_amt, max_amt)

        if amount > 0:
            add_item(resource, amount)
            print(f"+{amount} {resource}")
    