class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            while True:
                coins = input(f"How many {coin}?: ")
                try:
                    self.money_received += int(coins) * self.COIN_VALUES[coin]
                    break
                except:
                    print('Unknown command.')

        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            print(f'You have paid an amount equal to ${self.money_received}.')
            change = round(self.money_received - cost, 2)
            remainder = change
            if remainder > 0:
                print('Was returned:')

            if remainder >= 0.25:
                quaters_change = int(remainder / 0.25)
                remainder -= quaters_change * 0.25
                remainder = round(remainder, 2)
                print(f"  Quaters {quaters_change}")

            if remainder >= 0.10:
                dimes_change = int(remainder / 0.10)
                remainder -= dimes_change * 0.10
                remainder = round(remainder, 2)
                print(f"  Dimes {dimes_change}")

            if remainder >= 0.05:
                nickles_change = int(remainder / 0.05)
                remainder -= nickles_change * 0.05
                remainder = round(remainder, 2)
                print(f"  Nickles {nickles_change}")

            if remainder >= 0.01:
                pennies_change = int(remainder / 0.01)
                remainder -= pennies_change * 0.01
                remainder = round(remainder, 2)
                print(f"  Pennies {pennies_change}")


            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
        self.money_received = 0
