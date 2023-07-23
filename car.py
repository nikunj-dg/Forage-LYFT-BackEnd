from abc import ABC, abstractmethod
from datetime import datetime, date
from engine import *
from battery import *
from tire import *

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    @abstractmethod
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()

class CarFactory:
    def __init__(self) -> None:
        pass

    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = capuletEngine(current_mileage, last_service_mileage)
        battery = spindlerBattery(current_date, last_service_date)
        tire = carriganTire([0, 0, 0, 0])
        car = Car(engine, battery, tire)

        return car

    def create_glisade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        battery = spindlerBattery(current_date, last_service_date)
        tire = octoprimeTire([0, 0, 0, 0])
        car = Car(engine, battery, tire)

        return car

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = sternmanEngine(warning_light_on)
        battery = spindlerBattery(current_date, last_service_date)
        tire = carriganTire([0, 0, 0, 0])
        car = Car(engine, battery, tire)

        return car

    def create_rorshach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        battery = nubinBattery(current_date, last_service_date)
        tire = octoprimeTire([0, 0, 0, 0])
        car = Car(engine, battery, tire)

        return car

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = capuletEngine(current_mileage, last_service_mileage)
        battery = nubinBattery(current_date, last_service_date)
        tire = carriganTire([0, 0, 0, 0])
        car = Car(engine, battery, tire)

        return car
    



'''
__main__:

car_factory = CarFactory()
calliope = car_factory.create_calliope(...) 
'''


