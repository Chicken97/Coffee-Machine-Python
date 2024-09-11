class CoffeeMachine:
    def __init__(self):
        self.coffee_machine = {
            'water': 400,
            'milk': 540,
            'coffee_beans': 120,
            'cups': 9,
            'money': 550
         }
        self.state = 'choosing an action'

    def choose_action(self, action):
        if action == 'buy':
            self.buy()

        elif action == 'fill':
            self.fill()

        elif action == 'take':
            self.take()

        elif action == 'remaining':
            print(self)

        elif action == 'exit':
            exit()

    def __str__(self):
        return (f"\nThe coffee machine has:\n"
               f"{self.coffee_machine['water']} ml of water\n"
               f"{self.coffee_machine['milk']} ml of milk\n"
               f"{self.coffee_machine['coffee_beans']} g of coffee beans\n"
               f"{self.coffee_machine['cups']} disposable cups\n"
               f"${self.coffee_machine['money']} of money\n")

    def make_coffee(self, water, milk, coffee_beans, cost):

        if self.coffee_machine['water'] < water:
            print("Sorry, not enough water!")
        elif self.coffee_machine['milk'] < milk:
            print("Sorry, not enough milk!")
        elif self.coffee_machine['coffee_beans'] < coffee_beans:
            print("Sorry, not enough coffee beans")
        elif self.coffee_machine['cups'] < 1:
            print("Sorry, not enough cup")
        else:
            self.coffee_machine['water'] -= water
            self.coffee_machine['milk'] -= milk
            self.coffee_machine['coffee_beans'] -= coffee_beans
            self.coffee_machine['cups'] -= 1
            self.coffee_machine['money'] += cost
            print("I have enough resources, making you a coffee!\n")

    def buy(self):

        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back:\n")
        if choice == '1':
            self.make_coffee(250, 0, 16, 4)
        elif choice == '2':
            self.make_coffee(350, 75, 20, 7)
        elif choice == '3':
            self.make_coffee(200, 100, 12, 6)
        elif choice == 'back':
            return

    def fill(self):
        self.coffee_machine['water'] += int(input("Write how many ml of water you want to add:\n"))
        self.coffee_machine['milk'] += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_machine['coffee_beans'] += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.coffee_machine['cups'] += int(input("Write how many disposable cups you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.coffee_machine['money']}")
        self.coffee_machine['money'] = 0

machine = CoffeeMachine()

while True:
    user_input = input("Write action (buy, fill, take, remaining, exit):\n")
    machine.choose_action(user_input)
