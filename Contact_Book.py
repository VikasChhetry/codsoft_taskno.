class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            print("Contact List:")
            print("-------------")
            for contact in self.contacts:
                print(f"Name: {contact.name}\nPhone Number: {contact.phone_number}\nEmail: {contact.email}\nAddress: {contact.address}\n")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact.name or query in contact.phone_number]
        if not results:
            print("No contacts found!")
        else:
            print("Search Results:")
            for contact in results:
                print(f"Name: {contact.name}\nPhone Number: {contact.phone_number}\nEmail: {contact.email}\nAddress: {contact.address}\n")

    def update_contact(self, name, phone_number, email, address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = phone_number
                contact.email = email
                contact.address = address
                print(f"Contact {name} updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully!")
                return
        print("Contact not found!")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        match input("Enter your choice: "):
            case "1":
                name = input("Enter name: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                contact_manager.add_contact(name, phone_number, email, address)
            case "2":
                contact_manager.view_contact_list()
            case "3":
                query = input("Enter name or phone number to search: ")
                contact_manager.search_contact(query)
            case "4":
                name = input("Enter name of contact to update: ")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact_manager.update_contact(name, phone_number, email, address)
            case "5":
                name = input("Enter name of contact to delete: ")
                contact_manager.delete_contact(name)
            case "6":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()