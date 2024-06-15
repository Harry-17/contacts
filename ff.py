import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' added.")

def view_contacts():
    contacts = load_contacts()
    if contacts:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print("No contacts found.")

def search_contacts():
    name = input("Enter name to search: ")
    contacts = load_contacts()
    found_contacts = [contact for contact in contacts if name.lower() in contact['name'].lower()]
    if found_contacts:
        for idx, contact in enumerate(found_contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print(f"No contacts found with name '{name}'.")

def delete_contact():
    view_contacts()
    index = int(input("Enter the number of the contact to delete: ")) - 1
    contacts = load_contacts()
    if 0 <= index < len(contacts):
        removed_contact = contacts.pop(index)
        save_contacts(contacts)
        print(f"Contact '{removed_contact['name']}' deleted.")
    else:
        print("Invalid contact number.")

def main():
    while True:
        print("\nContact Management System")
        print("1. View contacts")
        print("2. Add contact")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
