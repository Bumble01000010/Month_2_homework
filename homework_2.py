class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        return f'Name: {self.name}, date of birth { self.birth_date}, skills: {self.occupation}, this man {'does' if self.higher_education else 'does not'} have a higher education.'

person_1 = Person('John "Hannibal" Smith', '01.10.1928', "Team leader, master tactician, and master of disguise", True)
person_2 = Person('Templeton Arthur "Faceman" Peck', '01.03.1945', "Con artist, smooth talker, and procurement expert", True)
person_3 = Person('H.M. (Howling Mad) Murdock', "24.11.1947", "Pilot extraordinaire; capable of flying almost any aircraft", True)
person_4 = Person('Bosco Albert "B.A." (Bad Attitude) Baracus', '21.05.1952', " Mechanic genius, heavy muscle and a driver ", False)

# print(person_1.introduce_1())
# print(person_2.introduce_1())
# print(person_3.introduce_1())
# print(person_4.introduce_1())


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, school_class):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = school_class

    def introduce(self):
        return f"my name is {self.name} and have studied in {self.group_name} class back in the day"


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        return f'{self.name} is friends with anyone who does {self.hobby}'


person_5 = Classmate("Joe", 1997, "doctor", True, "B" )
person_6 = Classmate("Duch", 2001, "baker", False, "A" )
person_7 = Friend("Mina", 1994, "concept artis", True, "work out")
person_8 = Friend("Rene", 1995, "mathematician ", True, "singing")

print(person_5.introduce())
print(person_6.introduce())

print(person_7.introduce())
print(person_8.introduce())



#________________________________________________________ Дополнительное задание 1 ____________________________
people_list = [person_5, person_6, person_7, person_8]

for i in people_list:
    print(i.introduce())

#________________________________________________________ Дополнительное задание 2 ____________________________

class BestFriends(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory ):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        parent_data = super().introduce()
        return(f'{parent_data}\n{self.name} shares the memory of {self.shared_memory} with alot of people')

person_9 = BestFriends('Ivan Drago', 1957, 'Boxer', True, "Training", 'bringing the glorious victory to soviet union')
person_10 = BestFriends('Draco Malfoy', 1960, "Wizard", True, "Being annoying", 'bringing the glorious victory to soviet union')

print(person_10.introduce())
print(person_9.introduce())