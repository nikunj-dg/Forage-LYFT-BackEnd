from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass

class carriganTire(Tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self) -> bool:
        for val in self.wear:
            if val >= 0.9:
                return True
        
        return False
        
class octoprimeTire(Tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self) -> bool:
        sum = 0
        for val in self.wear:
            sum += val
        
        if sum >= 3:
            return True
        
        return False