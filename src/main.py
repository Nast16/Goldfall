from engine.command_handler import handle_command

print("=== GOLDFALL ===")

while True:
    cmd = input("> ")
    handle_command(cmd)