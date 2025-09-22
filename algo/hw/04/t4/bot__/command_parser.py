def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    values = user_input.split()
    if len(values) == 2:
        return cmd, values[1]
    return cmd, *args