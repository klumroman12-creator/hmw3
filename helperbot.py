from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
     def __init__(self, value):
          if not (len(value) == 10 and value.isdigit()):
            raise ValueError('Номер телефону має містити 10 цифр')
          super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
         self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_nunber):
         self.phones = [p for p in self.phones if p.value != phone_nunber]

    def edit_phone(self, old_number, new_number):
         phone_obj = self.find_phone(old_number)
         if not phone_obj:
              raise ValueError(f"Номер {old_number} не знайдено")

         new_phone = Phone(new_number)

         idx = self.phones.index(phone_obj)
         self.phones[idx] = new_phone

    def find_phone(self, phone_number):
         for p in self.phones:
              if p.value == phone_number:
                   return p
         return None
         

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

# Пошук конкретного телефону в записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")




def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact not found."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args 
    _ = contacts[name]
    contacts[name] = phone
    return("Contact update!")
    

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return ("No contacts saved")
    
    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")

    return "\n".join(lines)



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
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


