from coffee import MENU, resources


def insert_amount():
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    dollars = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return dollars


def checking_recourses(choice):
    drink = MENU[choice]
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
        else:
            resources[ingredient] -= drink["ingredients"][ingredient]
            return True


def coffee_machine():
    money_in_coffee_machine = 0
    working_coffee_machine = True
    while working_coffee_machine:
        client_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if client_choice == "espresso" or client_choice == "latte" or client_choice == "cappuccino":
            if checking_recourses(client_choice):
                amount_paid = insert_amount()
                if amount_paid < MENU[client_choice]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                elif amount_paid > MENU[client_choice]["cost"]:
                    change = round(amount_paid - MENU[client_choice]["cost"], 2)
                    money_in_coffee_machine += MENU[client_choice]["cost"]
                    print(f"Here is ${change} dollars in change")
                    print(f"Here is you {client_choice}. Enjoy!")
                elif amount_paid == MENU[client_choice]["cost"]:
                    money_in_coffee_machine += MENU[client_choice]["cost"]
                    print(f"Here is you {client_choice}. Enjoy!")
        elif client_choice == "report":
            print(f"{resources['water']}ml")
            print(f"{resources['milk']}ml")
            print(f"{resources['coffee']}g")
            print(f"${money_in_coffee_machine}")
        elif client_choice == "off":
            working_coffee_machine = False
        else:
            print("Invalid choice.")


coffee_machine()
