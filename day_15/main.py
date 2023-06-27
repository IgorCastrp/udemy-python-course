MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


coins = {
    "quarter": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def report_machine():
    print(f"Water: {resources['water']}ml.\nMilk: {resources['milk']}ml.\nCoffee: {resources['coffee']}g."
          f"\nMoney: ${money}")


def update_resources(machine_resources, coffee):
    machine_resources.update({"water": resources["water"] - MENU[coffee]["ingredients"]["water"],
                              "milk": resources["milk"] - MENU[coffee]["ingredients"]["milk"],
                              "coffee": resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]})


def compare_espresso():

    water_espresso = MENU["espresso"]["ingredients"]["water"]
    coffee_espresso = MENU["espresso"]["ingredients"]["coffee"]
    water_machine = resources["water"]
    coffee_machine = resources["coffee"]

    if water_machine < water_espresso:
        print("Sorry, there is not enough water")
        return False
    elif coffee_machine < coffee_espresso:
        print("Sorry, there is not enough coffee")
        return False
    else:
        return True


def compare_latte():
    water_latte = MENU["latte"]["ingredients"]["water"]
    milk_latte = MENU["latte"]["ingredients"]["milk"]
    coffee_latte = MENU["latte"]["ingredients"]["coffee"]
    water_machine = resources["water"]
    coffee_machine = resources["coffee"]
    milk_machine = resources["milk"]

    if water_machine < water_latte:
        print("Sorry, there is not enough water")
        return False
    elif milk_machine < milk_latte:
        print("Sorry, there is not enough milk")
        return False
    elif coffee_machine < coffee_latte:
        print("Sorry, there is not enough coffee")
        return False
    else:
        return True


def compare_cappuccino():
    water_cappuccino = MENU["cappuccino"]["ingredients"]["water"]
    milk_cappuccino = MENU["cappuccino"]["ingredients"]["milk"]
    coffee_cappuccino = MENU["cappuccino"]["ingredients"]["coffee"]
    water_machine = resources["water"]
    coffee_machine = resources["coffee"]
    milk_machine = resources["milk"]

    if water_machine < water_cappuccino:
        print("Sorry, there is not enough water")
        return False
    elif milk_machine < milk_cappuccino:
        print("Sorry, there is not enough milk")
        return False
    elif coffee_machine < coffee_cappuccino:
        print("Sorry, there is not enough coffee")
        return False
    else:
        return True


def cost_coffee(coffee):
    if coffee == "espresso":
        return MENU["espresso"]["cost"]
    elif coffee == "latte":
        return MENU["latte"]["cost"]
    else:
        return MENU["cappuccino"]["cost"]


def payment(coffee):
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total_payment = quarters + dimes + nickels + pennies
    if coffee == "espresso":
        return total_payment - espresso_cost
    elif coffee == "latte":
        return total_payment - latte_cost
    else:
        return total_payment - cappuccino_cost


end_machine = False
money = 0
while not end_machine:

    get_coffee = input("\tWhat would you like? (espresso/latte/cappuccino): ").lower()

    if get_coffee == "off":
        end_machine = True
    elif get_coffee == "report":
        report_machine()
    elif get_coffee == "espresso":
        if compare_espresso():
            espresso_cost = cost_coffee("espresso")
            espresso_payment = payment("espresso")
            if espresso_payment < espresso_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                update_resources(resources, "espresso")
                money += espresso_cost
                print(f"Here is ${espresso_payment:.2f} in change.")
                print("Take your espresso, ☕. Enjoy!")
    elif get_coffee == "latte":
        if compare_latte():
            latte_cost = cost_coffee("latte")
            latte_payment = payment("latte")
            if latte_payment < latte_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                update_resources(resources, "latte")
                money += latte_cost
                print(f"Here is ${latte_payment:.2f} in change.")
                print("Take your latte, ☕. Enjoy!")
    elif get_coffee == "cappuccino":
        if compare_cappuccino():
            cappuccino_cost = cost_coffee("cappuccino")
            cappuccino_payment = payment("cappuccino")
            if cappuccino_payment < cappuccino_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                update_resources(resources, "cappuccino")
                money += cappuccino_cost
                print(f"Here is ${cappuccino_payment:.2f} in change.")
                print("Take your cappuccino, ☕. Enjoy!")


# TODO: 1. Ask the user what type the coffee he wants, after the action, ask again
# TODO: 2. Turn off the CoffeeMachine by entering "off" to the prompt
# TODO: 3. Print report when the user enters "report" in the prompt
# TODO: 4. Check if the resources are sufficient
# TODO: 5. Process coins (quarter: 0.25, dimes: 0.10, nickels: 0.05 and pennies: 0.01)
# TODO: 6. Check transaction
# TODO: 7. Make coffee
