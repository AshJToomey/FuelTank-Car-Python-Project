import unittest
from Encapsulation import FuelTank, Car

class TestFuelTank(unittest.TestCase):
    
    def setUp(self):
        self.tank = FuelTank(500, 1000)
        
    def test_fuel_up_valid(self):
        self.tank.fuel_up(200)
        self.assertEqual(self.tank.get_fuel(), 700)
        
    def test_fuel_up_exceed_capacity(self):
        self.tank.fuel_up(600)
        self.assertEqual(self.tank.get_fuel(), 500)
        
    def test_fuel_up_negative(self):
        self.tank.fuel_up(-100)
        self.assertEqual(self.tank.get_fuel(), 500)
        
    def test_drive_too_far(self):
        self.tank.drive(600)
        self.assertEqual(self.tank.get_fuel(), 500)
        
    def test_drive_negative(self):
        self.tank.drive(-10)
        self.assertEqual(self.tank.get_fuel(), 500)
        
    def test_get_fuel_percentage(self):
        self.assertAlmostEqual(self.tank.get_fuel_percentage(), 50.0)
        
class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.car = Car(400, 1000)
        
    def test_refuel_and_drive(self):
        self.car.refuel(300)
        self.assertEqual(self.car.check_fuel(), 700)
        self.car.drive(200)
        self.assertEqual(self.car.check_fuel(), 500)
        
    def test_drive_too_far(self):
        self.car.drive(800)
        self.assertEqual(self.car.check_fuel(), 400)
        
if __name__ == "__main__":
    unittest.main()