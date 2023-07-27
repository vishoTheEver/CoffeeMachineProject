# creating global variables or the quantity of things we have.
### This is for the operator
print("You are working as an operator!!!👷🏻")
MONEY = 0
# WATER = 300
WATER = int(input("What is the amount of water you're adding to the machine? "))
# MILK = 200
MILK = int(input("What is the amount of milk you're adding to the machine? "))
# COFFEE = 100
COFFEE = int(input("What is the amount of coffee you're adding to the machine? "))

### This is for the customer
print("\nNow, you are working as a customer.🙆🏻‍♂️")

# global variables for money
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

EXPRESSO = 1.5
LATTE = 2.5
CAPPUCCINO = 3

print("Menu\n-----\nExpresso: $1.50\nLatte: $2.50\nCappuccino: $3.0\n-----\nHit 'report' for remaining resources\n")



# some truths
is_the_coffee_on = True


# report statement
def report(f, g, h, i):
  print(f"Water: {f}ml")
  print(f"Milk: {g}ml")
  print(f"Coffee: {h}g")
  print(f"Money: ${i}")
  return


# money report
def calc_money():
  print("Please insert coins.")
  q = int(input("How many quarters?: "))
  d = int(input("How many dimes?: "))
  n = int(input("How many nickles?: "))
  p = int(input("How many pennies?: "))
  monetary_value = q * QUARTER + d * DIME + n * NICKEL + p * PENNY
  return monetary_value


# a while statement that shifts users until the program is manually terminated.
while is_the_coffee_on:
  choice_of_coffee = input("What would you like? (espresso/latte/cappuccino): ")
  # decision statements
  if choice_of_coffee == "off":
    is_the_coffee_off = False
  elif choice_of_coffee == "espresso":
    x = calc_money()
    if WATER < 50 or COFFEE < 18:
        if WATER < 50:
            print(f"Sorry there is not enough water.")
        if COFFEE < 18:
            print(f"Sorry there is not enough coffee.")
    else:
        if x > EXPRESSO:
            WATER = WATER - 50
            COFFEE = COFFEE - 18
            MONEY = MONEY + EXPRESSO

            print(f"Here is ${round(x - EXPRESSO, 2)} in change.")
            print("Here is your espresso ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
  elif choice_of_coffee == "latte":
    x = calc_money()
    if WATER < 200 or COFFEE < 24 or MILK < 150:
        if WATER < 200:
            print(f"Sorry there is not enough water.")
        if COFFEE < 24:
            print(f"Sorry there is not enough coffee.")
        if MILK < 150:
            print(f"Sorry there is not enough milk.")
    else:
        if x > LATTE:
            WATER = WATER - 200
            COFFEE = COFFEE - 24
            MILK = MILK - 150
            MONEY = MONEY + LATTE

            print(f"Here is ${round(x - LATTE, 2)} in change.")
            print("Here is your latte ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
  elif choice_of_coffee == "cappuccino":
    x = calc_money()
    if WATER < 250 or COFFEE < 24 or MILK < 100:
        if WATER < 250:
            print(f"Sorry there is not enough water.")
        if COFFEE < 24:
            print(f"Sorry there is not enough coffee.")
        if MILK < 100:
            print(f"Sorry there is not enough milk.")
    else:
        if x > CAPPUCCINO:
            WATER = WATER - 250
            COFFEE = COFFEE - 24
            MILK = MILK - 100
            MONEY = MONEY + CAPPUCCINO

            print(f"Here is ${round(x - CAPPUCCINO, 2)} in change.")
            print("Here is your cappuccino ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
  elif choice_of_coffee == "report":
      report(WATER, MILK, COFFEE, MONEY)
