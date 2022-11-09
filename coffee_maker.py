import time, random
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def coffee_process(self, coffee):
        if coffee == 'latte' or coffee == 'cappuccino':
            print("Preparing delicious espresso :)")
            time.sleep(random.randint(3, 5))
            print("Pour hot, delicious milk :)")
            time.sleep(random.randint(3, 5))
            print("We make foam for you :)")
            time.sleep(random.randint(3, 5))
        else:
            print("Preparing aromatic coffee :)")
            time.sleep(random.randint(3, 5))
            print("Fill everything with water.")
            time.sleep(random.randint(3, 5))

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️Enjoy!")
