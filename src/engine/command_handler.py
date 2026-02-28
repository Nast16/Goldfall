from system.gathering import gather

def handle_command(cmd):
    if cmd == "gather":
        gather()
    elif cmd == "exit":
        exit()
    else:
        print("Unknown command")