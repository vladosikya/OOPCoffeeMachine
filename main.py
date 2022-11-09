from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time, random

cap = '''
         
                        )     (
                 ___...(-------)-....___
             .-""       )    (          ""-.
       .-'``'|-._             )         _.-|
      /  .--.|   `""---...........---""`   |
     /  /    |                             |
     |  |    |                             |
      \  \   |                             |
       `\ `\ |                             |
         `\ `|                             |
         _/ /\                             /
        (__/  \                           /
     _..---""` \                         /`""---.._
  .-'           \                       /          '-.
 :               `-.__             __.-'              :
 :                  ) ""---...---"" (                 :
  '._               `"--...___...--"`              _.'
   \\""--..__                              __..--""/
     '._     """----.....______.....----"""     _.'
        `""--..,,_____            _____,,..--""`
                      `"""----"""`
'''

menu = Menu()
coffe_maker_main = CoffeeMaker()
profit = MoneyMachine()
COFFEMACHINE = True

while COFFEMACHINE:
    while True:
        choose = input(f'Hello. What coffee do you want? {menu.get_items()}').lower()
        if choose == 'latte':
            latte = menu.find_drink('latte')
            if coffe_maker_main.is_resource_sufficient(latte):
                if profit.make_payment(latte.cost):
                    coffe_maker_main.coffee_process('latte')
                    print(cap)
                    coffe_maker_main.make_coffee(latte)
        elif choose == 'espresso':
            espresso = menu.find_drink('espresso')
            if coffe_maker_main.is_resource_sufficient(espresso):
                if profit.make_payment(espresso.cost):
                    coffe_maker_main.coffee_process('espresso')
                    print(cap)
                    coffe_maker_main.make_coffee(espresso)
        elif choose == 'cappuccino':
            cappuccino = menu.find_drink('cappuccino')
            if coffe_maker_main.is_resource_sufficient(cappuccino):
                if profit.make_payment(cappuccino.cost):
                    coffe_maker_main.coffee_process('cappuccino')
                    print(cap)
                    coffe_maker_main.make_coffee(cappuccino)
        elif choose == 'exit':
            COFFEMACHINE = False
            break
        elif choose == 'replenish':
            while True:
                water = input('How many units to replenish water?')
                try:
                    coffe_maker_main.resources['water'] += int(water)
                    break
                except:
                    print('Unknown command!')
            while True:
                milk = input('How many units to replenish milk?')
                try:
                    coffe_maker_main.resources['milk'] += int(milk)
                    break
                except:
                    print('Unknown command!')
            while True:
                coffee = input('How many units to replenish coffee?')
                try:
                    coffe_maker_main.resources['coffee'] += int(coffee)
                    break
                except:
                    print('Unknown command!')
        elif choose == 'report':
            coffe_maker_main.report()
        elif choose == 'profit':
            profit.report()
        else:
            print("Unknown command.")