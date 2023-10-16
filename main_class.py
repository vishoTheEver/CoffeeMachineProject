class CoffeeMachine:
    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = 0

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")

    def calc_money(self):
        print("Please insert coins.")
        q = int(input("How many quarters?: "))
        d = int(input("How many dimes?: "))
        n = int(input("How many nickles?: "))
        p = int(input("How many pennies?: "))
        return q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01

    def make_coffee(self, water_req, milk_req, coffee_req, cost):
        if self.water < water_req:
            print("Sorry there is not enough water.")
            return
        if self.milk < milk_req:
            print("Sorry there is not enough milk.")
            return
        if self.coffee < coffee_req:
            print("Sorry there is not enough coffee.")
            return

        inserted_money = self.calc_money()
        if inserted_money < cost:
            print("Sorry that's not enough money. Money refunded.")
            return

        self.water -= water_req
        self.milk -= milk_req
        self.coffee -= coffee_req
        self.money += cost

        change = inserted_money - cost
        if change > 0:
            print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your coffee ☕️. Enjoy!")

def main():
    print("You are working as an operator!!!👷🏻")
    water = int(input("What is the amount of water you're adding to the machine? "))
    milk = int(input("What is the amount of milk you're adding to the machine? "))
    coffee = int(input("What is the amount of coffee you're adding to the machine? "))

    machine = CoffeeMachine(water, milk, coffee)

    print("\nNow, you are working as a customer.🙆🏻‍♂️")
    print("Menu\n-----\nExpresso: $1.50\nLatte: $2.50\nCappuccino: $3.0\n-----\nHit 'report' for remaining resources\n")

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            break
        elif choice == "espresso":
            machine.make_coffee(50, 0, 18, 1.5)
        elif choice == "latte":
            machine.make_coffee(200, 150, 24, 2.5)
        elif choice == "cappuccino":
            machine.make_coffee(250, 100, 24, 3)
        elif choice == "report":
            machine.report()

if __name__ == "__main__":
    main()
