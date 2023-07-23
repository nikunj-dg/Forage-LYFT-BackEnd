import unittest
from datetime import date
import sys

# adding (folder) to the system path
sys.path.insert(0, 'C:/Users/Acer/Box/Nikunj/Programmin/Forage/LYFT Back-End/My_Soln')

from car import *
from battery import *
from engine import *
from tire import *
#from utils import add_years_to_date

class testCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = capuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = capuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class testSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = sternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = sternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

class testWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = willoughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class testNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = nubinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = nubinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class testSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = spindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = spindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class testCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [0.6, 0.9, 1, 0.8]
        tire = carriganTire(wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear = [0.6, 0.4, 0.1, 0.5]
        tire = carriganTire(wear)
        self.assertTrue(tire.needs_service())

class testOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [0.8, 0.9, 1, 0.8]
        tire = octoprimeTire(wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear = [0.6, 0.3, 0.6, 0.5]
        tire = octoprimeTire(wear)
        self.assertTrue(tire.needs_service())






if __name__ == '__main__':
    unittest.main()
