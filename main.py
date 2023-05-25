from book import Book
from util import Util
from security import Security
import maskpass
my_book = Book()
security = Security()


if __name__ == '__main__':
    security.create_admin()
    while True:
        action = input("Commands: lg(login), cr(register), exit: ")
        if action == 'lg':
            user = input("Type username: ")
            password = maskpass.askpass()
            if security.login(user, password):
                print('You are login ' + user)
            else:
                print('You are not login ' + user)
        if action == 'cr':
            user = input("Type username: ")
            password = input("Type password: ")
            if security.create(user, password):
                print("User created")
            else:
                print("This user already exist")
        if action == 'exit':
            break

        if security.is_user_login():
            my_book.user_login = security.user_login
            admin = security.is_admin()
            if admin:
                while True:
                    action = input("Commands view(view users), del(remove users), exit: ")
                    if action == 'view':
                        security.draw()

                    if action == 'del':
                        name = input("User Name: ")
                        security.remove(name)

                    if action == 'exit':
                        security.logout()
                        break

            else:
                while True:
                    action = input("Commands (add, del, view, up, find, exit): ")
                    if action == 'add':
                        name = input("Person Name: ")
                        address = input("Address Name: ")
                        phones = input("Phone numbers: ")
                        if not Util.validate_phone_number(phones):
                            print("phone number must be numeric")
                            continue
                        result = my_book.create_contact(name, address, phones)
                        if result:
                            print("Create: " + name, "-", address, "-", phones)
                        else:
                            print("Name " + name + " already exist")
                    if action == 'up':
                        old_name = input("Person Name: ")
                        if my_book.exist_contact(old_name):
                            name = input("Update Name: ")
                            address = input("Update Address: ")
                            phones = input("Update phone number: ")
                            if not Util.validate_phone_number(phones):
                                print("phone number must be numeric")
                            result = my_book.update_contact(old_name, name, address, phones)
                            if result:
                                print("Update: " + name, "-", address, "-", phones)
                            else:
                                print("Name " + name + " already exist")
                        else:
                            print("Name " + old_name + " does not exist")
                    if action == 'del':
                        name = input("Person Name: ")
                        if my_book.delete_contact(name):
                            print("Name " + name + " remove")
                        else:
                            print("Name " + name + " does not exist")
                    if action == 'view':
                        my_book.draw_contacts()
                    if action == 'find':
                        name = input("Person Name: ")
                        c = my_book.exist_contact(name)
                        if c:
                            my_book.draw_one_contact(c)
                        else:
                            print("Name " + name + " does not exist")
                    if action == 'exit':
                        security.logout()
                        my_book.user_login = ''
                        break
