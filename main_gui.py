import PySimpleGUI as sg


class CoffeeMachine:
    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = 0

    def report(self):
        return f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}"

    def make_coffee(self, water_req, milk_req, coffee_req, cost, inserted_money):
        if self.water < water_req:
            return "Sorry there is not enough water."
        if self.milk < milk_req:
            return "Sorry there is not enough milk."
        if self.coffee < coffee_req:
            return "Sorry there is not enough coffee."
        if inserted_money < cost:
            return "Sorry that's not enough money. Money refunded."

        self.water -= water_req
        self.milk -= milk_req
        self.coffee -= coffee_req
        self.money += cost

        change = inserted_money - cost
        return_message = f"Here is your coffee ☕️. Enjoy!"
        if change > 0:
            return_message += f"\nHere is ${round(change, 2)} in change."

        return return_message

    def process_order(self, coffee_type, inserted_money):
        if coffee_type == "espresso":
            return self.make_coffee(50, 0, 18, 1.5, inserted_money)
        elif coffee_type == "latte":
            return self.make_coffee(200, 150, 24, 2.5, inserted_money)
        elif coffee_type == "cappuccino":
            return self.make_coffee(250, 100, 24, 3, inserted_money)


def main():
    machine = CoffeeMachine(300, 200, 100)

    layout = [
        [sg.Text("Welcome to the Coffee Machine!")],
        [sg.Button("Espresso"), sg.Button("Latte"), sg.Button("Cappuccino")],
        [sg.Button("Report"), sg.Button("Exit")]
    ]

    window = sg.Window("Coffee Machine", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event in ["Espresso", "Latte", "Cappuccino"]:
            coins_layout = [
                [sg.Text("Please insert coins.")],
                [sg.Text("Quarters:"), sg.InputText(key="quarters", size=(5, 1))],
                [sg.Text("Dimes:"), sg.InputText(key="dimes", size=(5, 1))],
                [sg.Text("Nickels:"), sg.InputText(key="nickels", size=(5, 1))],
                [sg.Text("Pennies:"), sg.InputText(key="pennies", size=(5, 1))],
                [sg.Button("Submit"), sg.Button("Cancel")]
            ]
            coins_window = sg.Window("Insert Coins", coins_layout)
            coin_event, coin_values = coins_window.read()
            coins_window.close()

            if coin_event == "Submit":
                try:
                    quarters = int(coin_values["quarters"])
                    dimes = int(coin_values["dimes"])
                    nickels = int(coin_values["nickels"])
                    pennies = int(coin_values["pennies"])
                except ValueError:
                    sg.PopupError("Please enter valid coin numbers.")
                    continue

                inserted_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
                message = machine.process_order(event.lower(), inserted_money)
                sg.Popup(message)
        elif event == "Report":
            sg.Popup(machine.report())

    window.close()


if __name__ == "__main__":
    main()
