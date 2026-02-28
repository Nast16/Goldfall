import random

gold = 0

def gather():
    global gold

    reward = random.randint(10, 30)
    gold += reward

    print(f"Kamu mengumpulkan resource.")
    print(f"+{reward} gold")
    print(f"Total gold: {gold}")
    