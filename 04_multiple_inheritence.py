# A Mixin is a class that provides methods, but NOT state.

# Meaning:

# It has NO __init__

# It does NOT store important attributes

# It only adds extra abilities (like logging, saving, printing, validation)

# It is meant to be used WITH another class through multiple inheritance

class EngineMixin:  # Mixin class for engine details
    def engine_info(self, horsepower):
        return f"Engine of {horsepower} HP"

class DriverMixin: # Mixin class for driver details
    def driver_info(self, name):
        return f"Mr. {name} is the driver."

class Car(EngineMixin, DriverMixin):    # Car class inheriting from both mixins (multiple inheritance)
    def __init__(self, model, horsepower, driver_name):
        self.model = model
        self.hp = horsepower
        self.driver = driver_name

    def race_info(self):
        return f"{self.driver_info(self.driver)} Driving {self.model} with {self.engine_info(self.hp)}."
    
car1 = Car("Ferrari", 650, "Lewis Hamilton")
print(car1.race_info()) # Using methods from both mixin classes