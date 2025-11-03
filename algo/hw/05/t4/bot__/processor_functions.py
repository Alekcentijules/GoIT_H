"""Module with command processing functions."""
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Provide name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments."
        except Exception as err:
            return f"Error: {err}"
    return inner

@input_error
def add_contact(args, contacts):
    """
    Adds a new contact.

    Args:
        args (List[str]): List of arguments: [name, phone]
        contacts (Dict[str, str]): Dictionary of contacts

    Returns:
        str: Message about the result
    """
    if len(args) != 2:
        return "Add requires name and phone."
    name, phone = args
    if not phone.isdigit():
        return "When adding a phone number, only digits should be entered."
    elif name in contacts:
        return "This contact was add."
    contacts[name] = phone
    return "Contact added!"

@input_error
def change_contact(args, contacts):
    """
    Changes the number of an existing contact.

    Args:
        args (List[str]): [name, new_number]
        contacts (Dict[str, str]): Dictionary of contacts

    Returns:
        str: Message about the result
    """
    if len(args) != 2:
        return "Change requires name and new phone."
    name, phone = args
    if name not in contacts:
        return "This contact isn't in list."
    elif not phone.isdigit():
        return "When adding a phone number, only digits should be entered."
    contacts[name] = phone
    return "Contact changed!"

@input_error
def output_phone(args, contacts):
    """
    Displays the phone number by name.

    Args:
        args (List[str]): [name]
        contacts (Dict[str, str]): Contact dictionary

    Returns:
        str: Phone number or error message
    """
    if len(args) != 2:
        return "Phone requires exactly one name."
    name = args[0]
    if name not in contacts:
        return "This contact isn't in list."
    return contacts[name]
