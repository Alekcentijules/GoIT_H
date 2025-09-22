from bot__ import parse_input
from bot__ import add_contact, change_contact, output_phone

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can i help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            command, arg = parse_input(user_input)
            print(output_phone(arg, contacts))
        elif command == "all":
            for name, phone in contacts.items():
                print(name, phone)
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()