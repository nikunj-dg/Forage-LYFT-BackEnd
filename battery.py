from abc import ABC, abstractmethod
from datetime import datetime, date
from car import *

class AbstractBattery(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass

class setBattery():
    def __init__(self, battery: AbstractBattery):
        self.battery = battery

    def needs_service(self) -> bool:
        return self.battery.needs_service()

class spindlerBattery(AbstractBattery):
    def __init__(self, current_date: date, last_service_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False

class nubinBattery(AbstractBattery):
    def __init__(self,  current_date: date, last_service_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False


'''
__main__:

battery = setBattery(spindlerBattery(...))
print("Service required : " + battery.needs_service())
'''


