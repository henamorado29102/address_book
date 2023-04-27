from contact import Contact
from data import load_data, save_data


class Book:

    def __init__(self):
        self.user_login = ''

    def create_contact(self, name, address, phones):
        contact = self.exist_contact(name)
        if contact:
            return False
        contact = Contact(name, address, phones)
        self.create(contact)
        return True

    def create(self, contact):
        contacts = load_data(self.user_login)
        contacts.append(contact)
        save_data(self.user_login, contacts)

    def delete_contact(self, name):
        return self.delete(name)

    def delete(self, name):
        contacts = load_data(self.user_login)
        for index, c in enumerate(contacts, start=0):
            if c.name == name:
                del contacts[index]
                save_data(self.user_login, contacts)
                return True
        return False

    def exist_contact(self, name):
        contacts = load_data(self.user_login)
        for c in contacts:
            if c.name == name:
                return c
        return False

    def update_contact(self, old_name, name, address, phones):
        exit_new_contact = self.exist_contact(name)
        if exit_new_contact:
            if exit_new_contact.name != old_name:
                return False
        self.delete(old_name)
        self.create(Contact(name, address, phones))
        return True

    def draw_contacts(self):
        contacts = load_data(self.user_login)
        for c in contacts:
            self.draw_one_contact(c)

    @staticmethod
    def draw_one_contact(c):
        print("Name: ", c.name, ", Address: ", c.address, ", Phone: ", c.phones)
