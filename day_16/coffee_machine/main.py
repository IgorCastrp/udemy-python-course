from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# ================  MY TRY  ================

# menu = Menu()
# money = MoneyMachine()
# coffee_maker = CoffeeMaker()
# end_machine = False
#
# while not end_machine:
#     choice = input(f"Choose your coffee: {menu.get_items()}:  ")
#
#     if choice == "off":
#         end_machine = True
#     elif choice == "report":
#         coffee_maker.report()
#     else:
#         item = menu.find_drink(choice)
#         print(coffee_maker.is_resource_sufficient(item))
#         money.process_coins()
#         if money.make_payment():
#             coffee_maker.make_coffee(item)

# ================  UDEMY CODE  ================

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
