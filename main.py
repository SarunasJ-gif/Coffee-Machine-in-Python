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
    if choice == "espresso":
        if MENU[choice]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water.")
            return False
        elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        else:
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            return True
    else:
        if MENU[choice]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water.")
            return False
        elif MENU[choice]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        else:
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            return True


def coffe_machine():
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
                    print(f"Here is you {client_choice}. Enjoy!")
                    money_in_coffee_machine += MENU[client_choice]["cost"]
        elif client_choice == "report":
            water = resources["water"]
            milk = resources["milk"]
            coffee = resources["coffee"]
            print(f"{water}ml")
            print(f"{milk}ml")
            print(f"{coffee}g")
            print(f"${money_in_coffee_machine}")
        elif client_choice == "off":
            working_coffee_machine = False
        else:
            print("Invalid choice.")


coffe_machine()
