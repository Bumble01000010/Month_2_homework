class A_Team:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce_1(self):
        ED_retun_value = lambda x: "this man does have higher education" if self.higher_education else "this man doesn't have higher education"
        return 'Name: {}, date of birth {}, skills: {}, {}.'.format(self.name, self.birth_date, self.occupation, ED_retun_value(self.higher_education))

person_1 = A_Team('John "Hannibal" Smith', '01.10.1928', "Team leader, master tactician, and master of disguise", True)
person_2 = A_Team('Templeton Arthur "Faceman" Peck', '01.03.1945', "Con artist, smooth talker, and procurement expert", True)
person_3 = A_Team('H.M. (Howling Mad) Murdock', "24.11.1947", "Pilot extraordinaire; capable of flying almost any aircraft", True)
person_4 = A_Team('Bosco Albert "B.A." (Bad Attitude) Baracus', '21.05.1952', " Mechanic genius, heavy muscle and a driver ", False)

# print(person_1.introduce_1())
# print(person_2.introduce_1())
# print(person_3.introduce_1())
# print(person_4.introduce_1())



class Classmate(A_Team):
    def __init__(self, name, birth_date, occupation, higher_education, school_class):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = school_class

    def introduce_1(self):
        return f"my name is {self.name} and have studied in {self.group_name} class back in the day"

    def is_classmate_whith_person_5(self):
        return f'My name is {self.name} and {"i am" if self.group_name == person_5.group_name else "i am not"} classmate of {person_5.name}'

class Friends(Classmate):
    def __init__(self, name, birth_date, occupation, higher_education, school_class, hobby):
        super().__init__(name, birth_date, occupation, higher_education, school_class)
        self.hobby = hobby

    def is_friend_whith_person_7(self):
        return f'{person_7.name} is {"a" if self.hobby == person_7.hobby else "not a"} friend of {person_7.name}'



person_5 = Classmate("Joe", 1997, "doctor", True, "B" )
person_6 = Classmate("Duch", 2001, "baker", False, "A" )
person_7 = Friends("Mina", 1994, "concept artis", True, "B", "Work out" )
person_8 = Friends("Rene", 1995, "mathematic ", True, "c",  "singing")

print(person_5.introduce_1())
print(person_6.is_classmate_whith_person_5())

print(person_7.introduce_1())
print(person_8.is_friend_whith_person_7())


#________________________________________________________ Дополнительное задание 1 ____________________________
people_list = [person_5, person_6, person_7, person_8]

for i in people_list:
    print(i.introduce_1())

#________________________________________________________ Дополнительное задание 2 ____________________________

class Best_friends(Friends):
    def __init__(self, name, birth_date, occupation, higher_education, school_class, hobby, shared_memory ):
        super().__init__(name, birth_date, occupation, higher_education, school_class, hobby)
        self.shared_memory = shared_memory

    def introduce_memory(self):
        return f'{self.name} and {person_9.name} share the wonderful memory of {self.shared_memory}'

person_9 = Best_friends('Ivan Drago', 1957, 'Boxer', True, "A", "Training", 'bringing the glorious victory to soviet union')
person_10 = Best_friends('Draco Malfoy', 1960, "Wizard", True, "slytherin ", "Being annoying",  'bringing the glorious victory to soviet union')

print(person_10.introduce_1())
print(person_9.introduce_1())
print(person_10.introduce_memory())