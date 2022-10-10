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
    "money": 0
}

def format_cost(MENU):
    return f"Espresso: ${MENU['espresso']['cost']}, Latte: ${MENU['latte']['cost']}, Cappuccino: ${MENU['cappuccino']['cost']},"

def format_report(resources):
    return f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['money']}"

def get_resources_for_coffee(choice):
    if choice == "espresso":
        water = MENU["espresso"]["ingredients"]["water"]
        milk = 0
        coffee = MENU["espresso"]["ingredients"]["coffee"]

    elif choice == "latte":
        water = MENU["latte"]["ingredients"]["water"]
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]

    elif choice == "cappuccino":
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    
    return (water, milk, coffee)

def can_we_make_coffee(choice):
    (water, milk, coffee) = get_resources_for_coffee(choice)

    if water > resources["water"]:
        return ("Sorry there isn't enough water.", False)
    elif milk > resources["milk"]:
        return ("Sorry there isn't enough milk.", False)
    elif coffee > resources["coffee"]:
        return ("Sorry there isn't enough coffee.", False)
    else:
        return ("", True)

def update_resources(choice):
    (water, milk, coffee) = get_resources_for_coffee(choice)

    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

def process_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    total = round(total, 2)
    return total

def is_transaction_possible(total, choice):
    if MENU[choice]["cost"] > total:
        return ("Sorry, that is not enough money. Money refunded.", False)
    else:
        return ("", True)

def update_money(total, choice):
    coffee_cost = MENU[choice]["cost"]
    change = 0

    if total > coffee_cost:
        change = round(total - coffee_cost)

    resources["money"] += coffee_cost
    return change
    
def main():
    is_machine_off = False

    while not is_machine_off:
        print(f"Welcome to Medha's Cafe!\n {format_cost(MENU)}")
        print("Type 'report' to get a list resources in the coffee machine and 'off' to turn off the coffee machine")
        choice = input("What would you like? espresso/latte/cappuccino: ")

        if choice == "report":
            print(format_report(resources))
        elif choice == "off":
            is_machine_off = True
        else:
            make_coffee = can_we_make_coffee(choice)
            if make_coffee[1]:
                total = process_coins()
                enough_money = is_transaction_possible(total, choice)
                if enough_money[1]:
                    update_resources(choice)
                    change = update_money(total, choice)
                    print("Here is ${:.2f} in change.".format(change))
                    print(f"Here is your {choice}. Enjoy!")
                else:
                    print(enough_money[0])
            else:
                print(make_coffee[0])

main()