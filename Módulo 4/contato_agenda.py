import csv
import contato

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.file_name = "contatos.csv"
        self.load_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def remove_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                found = True
                print(f"Contato {name} removido com sucesso!")
                break
        if found:
                self.save_contacts()
        else:
            print("Contato não encontrado.")


    def display_contacts(self):
        if not self.contacts:
            print("Lista de Contatos vazia.")
        else:
            for contact in self.contacts:
                print(contact)
                print("\n----------------------")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return
        print("Contato não encontrado.")

    def load_contacts(self):
        try:
            with open(self.file_name, 'r', newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.contacts.append(contato.Contact(row['name'], row['phone'], row['email']))
        except FileNotFoundError:
            pass
        
    def save_contacts(self):
        with open(self.file_name, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ['name', 'phone', 'email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({'name': contact.name, 'phone': contact.phone, 'email': contact.email})
                