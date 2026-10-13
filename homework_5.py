class Vehicle:
    def start(self):
        print('Vehicle starting')

class Car(Vehicle):
    def start(self):
        super().start()
        print('Car starting')

class ElectricCar(Vehicle):
    def ready(self):
        super().start()
        print('Electric car starting')

class Tesla(Car, ElectricCar):
    def start(self):
        super().start()
        print('Tesla ready')

model_Y = Tesla()
model_Y.start()