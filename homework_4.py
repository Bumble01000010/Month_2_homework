class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def  validate_phone_number(phone_number):
        if len(phone_number) == 10:
            return True
        else:
            return False


class ContactList:
    all_contacts = []
    @classmethod
    def add_contact(cls, name, phone_number):
        try:
            if Contact.validate_phone_number(phone_number) != True:
                raise ValueError
        except ValueError:
                print('Номер введен неправильно')
        else:
            ContactList.all_contacts.append(Contact(name, phone_number))



ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

ContactList.add_contact("John Doe", "5551234")


#_________________________________________________________________________________________________________


class Library:
    def __init__(self, city, books: list = None):
        self.city = city
        self.books = books

    def __str__(self):
        return f'Библиотека в городе {self.city}'

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        return item in self.books

lib = Library("Бишкек", books=["Война и мир", "1984", "Мастер и Маргарита"])
print(lib)
print(len(lib))
print("1984" in lib)
print("Гарри Поттер" in lib )

if len(lib) > 5:
    print("Библиотека большая (более 5 книг)")
else:
    print("Библиотека маленькая")