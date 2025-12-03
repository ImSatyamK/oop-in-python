from abc import ABC, abstractmethod

class Restaurant(ABC):

    @abstractmethod
    def prepare_food(self, dish):
        pass

    @abstractmethod
    def calculate_bill(self, dish):
        pass

class ItalianRestaurant(Restaurant):
    menu = {
        "pizza": 300,
        "pasta": 250
    }

    def prepare_food(self, dish):
        print(f"Making authentic Italian {dish} with olive oil and herbs...")

    def calculate_bill(self, dish):
        return self.menu.get(dish, 0)

class ChineseRestaurant(Restaurant):
    menu = {
        "noodles": 150,
        "momos": 120
    }

    def prepare_food(self, dish):
        print(f"Stir frying {dish} with soy sauce and veggies...")

    def calculate_bill(self, dish):
        return self.menu.get(dish, 0)
    
# Here each restaurant decides its own:

# Cooking style

# Pricing system

# Ingredients

# The main system does not need to know the internal cooking logic.

def order_food(restaurant: Restaurant, dish: str):
    print(f"Ordering {dish}...")
    restaurant.prepare_food(dish)
    amount = restaurant.calculate_bill(dish)
    print(f"Bill Amount: ₹{amount}")
    print("Food is ready for delivery!\n")


# Objects
italian = ItalianRestaurant()
chinese = ChineseRestaurant()

# Orders
order_food(italian, "pizza")
order_food(chinese, "noodles")

# ✔ What abstraction is doing here
# The ordering system knows only:

# Restaurant must have prepare_food()

# Restaurant must have calculate_bill()

# The ordering system does not know:

# How cooking happens

# What ingredients are used

# How menu prices are stored

# How the bill is calculated

# That entire messy logic is abstracted away.