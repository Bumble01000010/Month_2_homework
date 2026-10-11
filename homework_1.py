class AteamIntro:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):

        return f'Name: {self.name}, date of birth { self.birth_date}, skills: {self.occupation}, this man {'does' if self.higher_education else 'does not'} have a higher education.'

leader = AteamIntro('John "Hannibal" Smith', '01.10.1928', "Team leader, master tactician, and master of disguise", True)
spy = AteamIntro('Templeton Arthur "Faceman" Peck', '01.03.1945', "Con artist, smooth talker, and procurement expert", True)
pilot = AteamIntro('H.M. (Howling Mad) Murdock', "24.11.1947", "Pilot extraordinaire; capable of flying almost any aircraft", True)
driver = AteamIntro('Bosco Albert "B.A." (Bad Attitude) Baracus', '21.05.1952', " Mechanic genius, heavy muscle and a driver ", False)

print(leader.introduce())
print(spy.introduce())
print(pilot.introduce())
print(driver.introduce())