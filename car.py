from abc import ABC, abstractmethod
from datetime import datetime, date
from engine import *
from battery import *

class AbstractCar(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass 

class CalliopeCar(AbstractCar):
    def __init__(self, engine, battery):
        self.engine = engine # Capulet 
        self.battery = battery # Spindler 

    def needs_service(self) -> bool:
        pass

class GlisadeCar(AbstractCar):
    def __init__(self, engine, battery):
        self.engine = engine # Willoughby 
        self.battery = battery # Spindler 

    def needs_service(self) -> bool:
        pass

class PalindromeCar(AbstractCar):
    def __init__(self, engine, battery):
        self.engine = engine  # Sternman
        self.battery = battery  # Spindler

    def needs_service(self) -> bool:
        pass

class RorshachCar(AbstractCar):
    def __init__(self, engine, battery):
        self.engine = engine  # Willoughby 
        self.battery = battery  # Nubin

    def needs_service(self) -> bool:
        pass

class ThovexCar(AbstractCar):
    def __init__(self, engine, battery):
        self.engine = engine  # Capulet
        self.battery = battery  # Nubin

    def needs_service(self) -> bool:
        pass
        
class CreateCalliope(CarFactory):
    def create_car(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> AbstractCar:
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        return CalliopeCar()

class CreateGlisade(CarFactory):
    def create_car(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> AbstractCar:
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        return CalliopeCar()

class CreatePalindrome(CarFactory):
    def create_car(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> AbstractCar:
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        return CalliopeCar()

class CreateRorshach(CarFactory):
    def create_car(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> AbstractCar:
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        return CalliopeCar()

class CreateThovex(CarFactory):
    def create_car(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> AbstractCar:
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        return CalliopeCar()



