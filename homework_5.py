class Vehicle:
    def start(self):
        print('Vehicle starting')

class Car(Vehicle):
    def start(self):
        super().start()
        print('Car starting')

class ElectricCar(Car):
    def ready(self):
        super().start()
        print('Electric car ready')

class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print('Tesla starting')

model_Y = Tesla()
model_Y.start()