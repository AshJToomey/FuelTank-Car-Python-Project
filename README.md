# FuelTank & Car Python Project

## Overview

This project demonstrates core Object-Oriented Programming (OOP) concepts in Python through a simple model of a car's fuel tank management system. It includes:

- Encapsulation of private attributes
- Input validation with user-friendly logging
- Composition (Car has a FuelTank)
- Methods to refuel, drive, and check fuel levels
- Unit tests to ensure functionality correctness

---

## Features

- **FuelTank class**: manages fuel amount and capacity with private attributes.
- **Car class**: interacts with the FuelTank for driving and refueling.
- Validation prevents overfilling and driving beyond available fuel.
- Warnings logged for low fuel and invalid operations.
- Calculates current fuel percentage.

---

## Usage

```python
from your_module import Car

car = Car(1000, 2000)   # initial fuel = 1000, capacity = 2000
car.refuel(500)
car.drive(200)

print("Fuel left:", car.check_fuel())             # e.g., 1300
print("Fuel % left:", car.check_fuel_percentage()) # e.g., 65.0


## Running Tests
Tests are written using Python's built-in unittest framework.

Run the tests with:

python -m unittest test_fuelcar.py

## Requirements
Python 3.x

## Project Structure

├── Encapsulation.py         # FuelTank and Car class definitions

├── test_fuelcar.py          # Unit tests for the project

├── README.md                # This file

## Contributing
Feel free to open issues or submit pull requests to improve this project.

## License
MIT License
