from abc import ABC, abstractmethod
from datetime import datetime
from car import *

class AbstractBattery(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass

class SpindlerBatter(AbstractBattery):
    def __init__(self):
        pass

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False

class NubinBattery(AbstractBattery):
    def __init__(self):
        pass

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False