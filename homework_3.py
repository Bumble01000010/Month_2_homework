TRIP_COST = 20

class TransportCard():
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self):
        print(f'Владельца данного баланса зовут {self.__owner}')

    def get_balance(self):
        print(self.__balance)

    def addmoney(self, money):
        if money <= 0:
            print('Сумма пополнения должна быть положительной')
            return
        self.__balance = self.__balance + money
        print(f'Ваш баланс был пополнен  на {money}')


    def pay_for_trip(self):
        if self.__balance <= TRIP_COST:
            print('На балансе недостаточно средств')
            return

        self.__balance = self.__balance - TRIP_COST
        print('Куплен один билет')


passenger_1 = TransportCard("Maurice", 0)
passenger_2 = TransportCard("Krill", 10)

passenger_1.get_owner()
passenger_1.get_balance()
passenger_1.addmoney(50)
passenger_1.get_balance()
passenger_1.pay_for_trip()
passenger_1.get_balance()
passenger_1.pay_for_trip()
passenger_1.get_balance()