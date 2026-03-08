from engine.market import update_market
from engine.events import trigger_event

TICK_INTERVAL = 5

world_state = {
    "tick_count": 0
}


def world_tick():
    world_state["tick_count"] += 1

    if world_state["tick_count"] >= TICK_INTERVAL:
        print("\n Dunia berubah...")
        update_market()
        trigger_event()
        world_state["tick_count"] = 0