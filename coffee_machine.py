# Write your code here
# database
ingredients = {'water': ['ml', 'ml'],
               'milk': ['ml', 'ml'],
               'coffee beans': ['g', 'grams'],
               'disposable cups': ['', '']}
recipe = {'espresso': {'water': 250, 'coffee beans': 16},
          'latte': {'water': 350, 'milk': 75, 'coffee beans': 20},
          'cappuccino': {'water': 200, 'milk': 100, 'coffee beans': 12}}


class CoffeeMachine:
    def __init__(self):
        self.storage = {'water': 400,
                        'milk': 540,
                        'coffee beans': 120,
                        'disposable cups': 9}
        self.money = 550
        self.price = {'espresso': 4,
                      'latte': 7,
                      'cappuccino': 6}
        self.menu()

    def menu(self):
        print()
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == 'buy':
            self.buy_menu()
        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'remaining':
            self.remaining()
        elif action == 'exit':
            exit()
        else:
            self.menu()

    def remaining(self):
        print("The coffee machine has:")
        for el in self.storage:
            print(f"{self.storage[el]} of {el}")
        print(f"${self.money} of money")
        self.menu()

    def fill(self):
        print()
        for ing in self.storage:
            print(f"Write how many {ingredients[ing][1]} of {ing} do you want to add:")
            self.storage[ing] += int(input())
        self.menu()
        pass

    def take(self):
        print()
        print(f"I gave you ${self.money}")
        self.money = 0
        self.menu()
        pass

    def buy_menu(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        action = input()
        if action == '1':
            self.buy_coffee('espresso')
        elif action == '2':
            self.buy_coffee('latte')
        elif action == '3':
            self.buy_coffee('cappuccino')
        elif action == 'back':
            self.menu()
        else:
            self.buy_menu()

    def buy_coffee(self, drink):
        if self.check_storage(drink):
            print("I have enough resources, making you a coffee!")
            for ingredient in recipe[drink]:
                self.storage[ingredient] -= recipe[drink][ingredient]
            self.storage['disposable cups'] -= 1
            self.money += self.price[drink]
        self.menu()

    def check_storage(self, drink):
        if self.storage['disposable cups'] == 0:
            print(f"Sorry, not enough disposable cups!")
            return False
        else:
            for el in recipe[drink]:
                amount = self.storage[el] // recipe[drink][el]
                if amount == 0:
                    print(f"Sorry, not enough {el}!")
                    return False
                else:
                    return True


number_one = CoffeeMachine()
