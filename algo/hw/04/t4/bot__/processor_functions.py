def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "This contact was add."
    contacts[name] = phone
    return "Contact added!"

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed!"

def output_phone(arg, contacts):
    return contacts[arg]
