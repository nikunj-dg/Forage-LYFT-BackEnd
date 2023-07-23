from abc import ABC, abstractmethod 

class Engine(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class capuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000

class willoughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000

class sternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        if self.warning_light_is_on:
            return True
        else:
            return False


'''
__main__:

engine = capuletEngine(...)
print("Service required : " + engine.needs_service())
'''


