from abc import ABC, abstractmethod
from datetime import datetime, date
from engine import *
from battery import *

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class AbstractCar(Serviceable):
    @abstractmethod
    def __init__(self):
        pass

class CarFactory():
    def __init__(self) -> None:
        pass

    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> AbstractCar:
        return CalliopeCar(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_glisade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> AbstractCar:
        return GlisadeCar(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> AbstractCar:
        return PalindromeCar(current_date, last_service_date, warning_light_on)

    def create_rorshach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> AbstractCar:
        return RorshachCar(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> AbstractCar:
        return ThovexCar(current_date, last_service_date, current_mileage, last_service_mileage)
    
class CalliopeCar(AbstractCar):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.engine = setEngine(capuletEngine(current_mileage, last_service_mileage))
        self.battery = setBattery(spindlerBattery(current_date, last_service_date))

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class GlisadeCar(AbstractCar):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.engine = setEngine(willoughbyEngine(current_mileage, last_service_mileage))
        self.battery = setBattery(spindlerBattery(current_date, last_service_date))

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class PalindromeCar(AbstractCar):
    def __init__(self, current_date: date, last_service_date: date, warning_light_on: bool):
        self.engine = setEngine(sternmanEngine(warning_light_on))
        self.battery = setBattery(spindlerBattery(current_date, last_service_date))

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class RorshachCar(AbstractCar):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.engine = setEngine(qilloughbyEngine(current_mileage, last_service_mileage))
        self.battery = setBattery(nubinBattery(current_date, last_service_date))

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class ThovexCar(AbstractCar):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.engine = setEngine(capuletEngine(current_mileage, last_service_mileage))
        self.battery = setBattery(nubinBattery(current_date, last_service_date))

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()


'''
__main__:

car_factory = CarFactory()
calliope = car_factory.create_calliope(...) 
'''


