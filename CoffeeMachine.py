# ☕
# Penny = 1 cent $0.01 | neckel = 5 cent $0.05 | dime = 10 cent $0.10 | Quarter = 25 cents $0.25
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
            "water": 200,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}
resources = {"water": 300, "milk": 200, "coffee": 100}

profit = 0

def is_ingredient_sufficient(ingredients):
    """Return True when order can be made, False if ingredients are insufficient."""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.") 
            return False
    return True

def process_coins():
    """Return total calculated coins."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.")
        return False

def generate_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕.")

while True:
    choose_coffee = input("What would you like (espresso/latte/cappuccino): ")

    if choose_coffee == 'off':
        break
    elif choose_coffee == 'report':
        generate_report(resources)
    else:
        drink = MENU[choose_coffee]
        if is_ingredient_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction(payment, drink["cost"]):
                make_coffee(choose_coffee, drink["ingredients"])