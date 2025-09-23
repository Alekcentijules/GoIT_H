def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    values = user_input.split()
    if len(values) == 2:
        return cmd, values[1]
    elif values[2] not in "0123456789":
        return "When adding a phone number, only digits should be entered."
    return cmd, *args