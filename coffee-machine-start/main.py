from menu import MENU, resources

money = 0
def money_check(quarters, dimes, nickles, pennies):
  result = (0.01 * pennies)+ (0.05 * nickles) + (0.1 * dimes) + (0.25 * quarters)
  return result

def insert_money(coffee_money):
  print("Please insert coins.")
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickles?: "))
  pennies = int(input("How many pennies?: "))
  if money_check(quarters, dimes, nickles, pennies) >= coffee_money:
    return True
  else:
    return False
    

question = input("What would you like? (espresso, latte, cappuccino): ").lower()

if question == "report":
  print(f'Water: {resources["water"]}ml')
  print(f'Milk: {resources["milk"]}ml')
  print(f'Coffee: {resources["coffee"]}ml')
  print(f"Money: ${money}")

elif question == "espresso" and resources["water"]>=50 and resources["coffee"]>=18:
  
  if insert_money(1.5):
    resources["water"] -=50
    resources["coffee"] -=18
    money += 1.5
    
elif question == "latte" and resources["water"]>=200 and resources["coffee"]>=24 and resources["milk"] >=150:
  
  if insert_money(2.5):
    resources["water"] -=200
    resources["coffee"] -=24
    resources["milk"] -=150
    money += 2.5
    
elif question == "cappuccino" and resources["water"]>=200 and resources["coffee"]>=24 and resources["milk"] >=150:
  
  if insert_money(3.0):
    resources["water"] -=250
    resources["coffee"] -=24
    resources["milk"] -=100
    money += 3.0
    
else:
  print("Error")