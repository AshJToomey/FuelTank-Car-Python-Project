def log(message):
    print(f"[LOG] {message}")    

class FuelTank:
    def __init__(self, fuel, capacity):
        self.__fuel = fuel  # private
        self.__capacity = capacity
        
    def fuel_up(self, amount):
        if amount > 0:
            if self.__fuel + amount <= self.__capacity:
                 self.__fuel += amount
            else:
               log("Cannot exceed fuel tank capacity.")
        else:
            log("Tank must have a positive fuel value.")
    def drive(self, amount):
        if amount <= 0:
            log("Drive amount must be postive")
           
        elif amount > self.__fuel:
             log("Not enough fuel to drive that far.")
        else:
            self.__fuel -= amount
            
    def get_fuel(self):
        if self.__fuel < 100:
            log("Warning: Low fuel level!")
        return self.__fuel

    def get_fuel_percentage(self):
        return (self.__fuel / self.__capacity) * 100

class Car:
    def __init__(self, fuel, capacity):
        self.tank = FuelTank(fuel, capacity)
    
    def drive(self, distance):
        self.tank.drive(distance)
        
    def refuel(self, amount):
        self.tank.fuel_up(amount)

    def check_fuel(self):
        return self.tank.get_fuel()
    
    def check_fuel_percentage(self):
        return self.tank.get_fuel_percentage()

car = Car(1000, 2000)
car.refuel(500)
car.drive(200)
print("Fuel left:", car.check_fuel())  # 1300
print("Fuel % left:", car.check_fuel_percentage())