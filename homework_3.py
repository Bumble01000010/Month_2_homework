TRIP_COST = 20

class TransportCard():
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self):
        print(f'Владельца данного баланса зовут {self.__owner}')

    def get_balance(self):
        print(f'На данном балансе {self.__balance}')

    def addmoney(self, money):
        try:
            if money <= 0:
                raise ValueError
        except ValueError:
            print('Баланс можно пополнить на сумму выше 0')
        else:
            self.__balance = self.__balance + money
            print(f'Ваш баланс был пополнен  на {money}')


    def pay_for_trip(self):
        try:
            if self.__balance < TRIP_COST:
                raise ValueError
        except ValueError:
                print(f'На сету {self.__owner} недостаточно средств')
        else:
            self.__balance = self.__balance - TRIP_COST
            print('Куплен один билет')


passenger_1 = TransportCard("Maurice", 0)
passenger_2 = TransportCard("Krill", 0)

passenger_1.get_owner()
passenger_1.get_balance()
passenger_1.addmoney(-5)
passenger_1.addmoney(60)
passenger_1.get_balance()
passenger_1.pay_for_trip()
passenger_1.get_balance()
passenger_1.pay_for_trip()
passenger_1.get_balance()

passenger_2.get_owner()
passenger_2.get_balance()
passenger_2.addmoney(30)
passenger_2.get_balance()
passenger_2.addmoney(10)
passenger_2.pay_for_trip()
passenger_2.pay_for_trip()
passenger_2.get_balance()