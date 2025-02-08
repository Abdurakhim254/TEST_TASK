print("Hello World")
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        return f"{super().display_info()} - {self.fuel_type}"


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year, "Electric")
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{super().display_info()} - {self.battery_capacity} kWh battery"


# Example usage
car1 = Car("Toyota", "Camry", 2022, "Gasoline")
ev1 = ElectricCar("Tesla", "Model 3", 2023, 75)

print(car1.display_info())  # Output: 2022 Toyota Camry - Gasoline
print(ev1.display_info())   # Output: 2023 Tesla Model 3 - Electric - 75 kWh battery
