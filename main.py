from coffee_data import MENU


water=300
milk=200
coffee=100
money=0

def main_menu_function():
    print("Rate List:\n 1.Espresso ₹30\n 2.Latte ₹40\n 3.Cappuccino ₹50")
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    print()
    return choice

def check_resources(choice,water,milk,coffee):
    required_water=MENU[choice]['ingredients']['water']
    required_milk=MENU[choice]['ingredients']['milk']
    required_coffee=MENU[choice]['ingredients']['coffee']
    if required_water>water:
        print(f"Sorry there is not enough water")
    elif required_milk>milk:
        print(f"Sorry there is not enough milk")
    elif required_coffee>coffee:
        print(f"Sorry there is not enough coffee")
    else:
        return True
    
def insert_coins():
    print("Please insert coins")
    fifty_count=int(input("How many fifty?: "))
    twenty_count=int(input("How many twenty?: "))
    tens_count=int(input("How many tens?: "))
    print()
    return (fifty_count*50+twenty_count*20+tens_count*10)

def make_coffee_function(choice,water,milk,coffee,money):
    if choice=="off":
        return 0
    elif choice=="report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ₹{money}\n")
        make_coffee_function(choice=main_menu_function(),water=water,milk=milk,coffee=coffee,money=money)
    else:
        if(check_resources(choice,water,milk,coffee)):
            amount=insert_coins()
            if amount<MENU[choice]['cost']:
                print("Sorry that is not enough money, Money refunded")
            
            elif amount>MENU[choice]['cost']:
                print(f"Here is ₹{amount-MENU[choice]['cost']} in change")
            
            print(f"Here is your {choice} ☕. Enjoy!")
            required_water=MENU[choice]['ingredients']['water']
            required_milk=MENU[choice]['ingredients']['milk']
            required_coffee=MENU[choice]['ingredients']['coffee']
            water-=required_water
            milk-=required_milk
            coffee-=required_coffee
            money+=MENU[choice]['cost']
            print()
        make_coffee_function(choice=main_menu_function(),water=water,milk=milk,coffee=coffee,money=money)
        


            

        
make_coffee_function(main_menu_function(),water,milk,coffee,money)
    
