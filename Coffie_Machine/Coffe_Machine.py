Menu = {
    "lattee": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 20,
        },
        "cost": 150
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 25,
            },
        "cost": 100
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 50
    }
}
# print(Menu)
resources = {
    "water": 600,
    "milk": 500,
    "coffee": 150	
}
profit = 0

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("Please insert coins.")
    total = 0
    coins_five = int(input("How many 5rs coins?: "))
    coins_ten = int(input("How many 10rs coins?: "))
    coins_twenty = int(input("How many 20rs coins?: "))
    total = coins_five*5 + coins_ten*10+coins_twenty*20
    return total

def is_payment_successful(money_received,coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit +=coffee_cost
        change = money_received - coffee_cost
        if change == 0:
            print("Exact amount received, No change")
            return True
        elif change > 0:
            print(f"Here is your Rs{change} in change")
            return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False

def make_coffee(coffee_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name}, Have a good day!")
    
is_on = True
while is_on:
    choice = input("What would You like to have('lattee'/'cappuccino'/'espresso'): ").lower()
    if choice == "off": 
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money = Rs{profit}")
    # elif choice != Menu[choice]:
    #     coffee_type = Menu[choice]
    #     print("Invalid Input!!, Please try again")
    elif choice == "cappuccino" or "lattee" or "espresso":
        coffee_type = Menu[choice]
        print(f"cost of {choice} is {coffee_type['cost']}\n")
        # print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])