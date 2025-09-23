def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "This contact was add."
    elif not phone.isdigit():
        return "When adding a phone number, only digits should be entered."
    contacts[name] = phone
    return "Contact added!"

def change_contact(args, contacts):
    name, phone = args
    if not name in contacts:
        return "This contact isn't in list."
    elif not phone.isdigit():
        return "When adding a phone number, only digits should be entered."
    contacts[name] = phone
    return "Contact changed!"

def output_phone(arg, contacts):
    if not arg in contacts:
        return "This contact isn't in list."
    return contacts[arg]
