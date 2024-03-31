import re

def cms():

    contacts = {
        "John Doe": {"E-mail Address": "johndoe@gmail.com", "Phone": "256-123-1234", "Address": "123 Grove Circle"},
        "Jane Smith": {"E-mail Address": "janesmith@gmail.com", "Phone": "256-123-6789", "Address": "343 Dunbar Drive"},
        "Jimmy Gallop": {"E-mail Address": "jimmygallop@gmail.com", "Phone": "314-159-0000", "Address": "111 Fly Boulevard"}
    }

    try:
        while True:
            menu = input("""
            Welcome to the Contact Management System!

            Menu:
            1. Add a new contact
            2. Edit an existing contact
            3. Delete a contact
            4. Search for a contact
            5. Display all contacts
            6. Export contacts to a text file
            7. Quit
                         
            Please enter a selection: """)

            if menu == "1":
                contacts = add_contact(contacts)
            elif (menu) == "2":
                edit_contact(contacts)
            elif (menu) == "3":
                contacts = delete_contact(contacts)
            elif (menu) == "4":
                search_contacts(contacts)
            elif menu == "5":
                  display_contacts(contacts)
            elif menu == "6":
                  export_contacts(contacts)
            elif menu == "7":
                break
            else:
                print("Sorry, that is not a valid selection. Please try again.")
    except (OverflowError, TypeError, ValueError):
        print("Sorry, that is not a valid selection. Please try again.")
    finally:
        print("Thank you for using this application. Goodbye!")

    return contacts

def add_contact(contacts):

    while True:
        contact_name = input("Please enter the contact's full name: ")
        if re.match(r"[A-Z][a-z]+ [A-Z][a-z]+", contact_name):
            break
        else:
            print("Sorry, that is not a valid name. The format must be 'Firstname Lastname.' Please try again.")
    contacts[contact_name] = {"E-mail Address": "", "Phone": "", "Address": ""}

    while True:
        contact_email = input("Please enter the contact's e-mail address: ")
        if re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", contact_email):
            break
        else:
            print("Sorry, that is not a valid e-mail address. Please try again.")
    contacts[contact_name]["E-mail Address"] = contact_email

    while True:
        contact_phone = input("Please enter the contact's phone number: ")
        if re.match(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", contact_phone):
            break
        else:
            print(f"Sorry, that is not a valid phone number. The format must be 'XXX-XXX-XXXX.' Please try again.")
    contacts[contact_name]["Phone"] = contact_phone
    
    while True:
        contact_address = input("Please enter the contact's address: ")
        contacts[contact_name]["Address"] = contact_address
        print(f"You have successfully added {contact_name} to the Contact Management System.")
        return contacts

def edit_contact(contacts):
    select_name = input("Please enter the full name of the contact that you would like to edit: ")
    if select_name in contacts:
        edit_choice = input("""
        What would you like to edit?                    

        1. The contact's name
        2. The contact's e-mail address
        3. The contact's phone number
        4. The contact's address
                            
        Please enter a selection: """)

        if edit_choice == "1":
            while True:
                new_name = input(f"Please enter a new full name for {select_name}: ")
                if re.match(r"[A-Z][a-z]+ [A-Z][a-z]+", select_name):
                    break
                else:
                    print("Sorry, that is not a valid name. The format must be 'Firstname Lastname.' Please try again.")
            contacts[select_name] = new_name
            print(f"You have successfully updated the contact info for {new_name}.")
            return contacts
            
        elif edit_choice == "2":
            while True:
                new_email = input(f"Please enter a new e-mail address for {select_name}: ")
                if re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", new_email):
                    break
                else:
                    print("Sorry, that is not a valid e-mail address. Please try again.") 
            contacts[select_name]["E-mail Address"] = new_email
            print(f"You have successfully updated the contact info for {select_name}.")
            return contacts

        elif edit_choice == "3":
            while True:
                new_phone = input(f"Please enter a new phone number for {select_name}: ")
                if re.match(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", new_phone):
                    break
                else:
                    print(f"Sorry, that is not a valid phone number. The format must be 'XXX-XXX-XXXX.' Please try again.")
            contacts[select_name]["Phone"] = new_phone
            print(f"You have successfully updated the contact info for {select_name}.")
            return contacts
            
        elif edit_choice == "4":
                new_address = input(f"Please enter a new address for {select_name}: ")
                contacts[select_name]["Address"] = new_address
                print(f"You have successfully updated the contact info for {select_name}.")
                return contacts
        else:
            print("Sorry, that is not a valid selection. Please try again.")
    else:
        print(f"Sorry, {select_name} does not exist in the Contact Management System. Please try again.")

def delete_contact(contacts):
    goner = input("Please enter the full name of the contact that you would like to delete: ")
    if goner in contacts:
        contacts.pop(goner)
        print(f"You have successfully deleted {goner} from the Contact Management System.")
        return contacts
    else:
        print(f"Sorry, {goner} does not exist in the Contact Management System. Please try again.")

def search_contacts(contacts):
    waldo = input("Please enter the full name of the contact that you would like to find: ")
    if waldo in contacts:
        print(contacts[waldo])
    else:
        print(f"Sorry, {waldo} does not exist in the Contact Management System. Please try again.")

def display_contacts(contacts):
    sorted_contacts = sorted(contacts.items())
    for contact, details in sorted_contacts:
        print(f"{contact}: {details}")

def export_contacts(contacts):
    file_name = "Contacts.txt"
    with open(file_name, "w") as file:
        for contact, details in contacts.items():
            file.write(f"{contact}: {details}\n")
    print(f"You have successfully exported your contacts to {file_name}.")

cms()