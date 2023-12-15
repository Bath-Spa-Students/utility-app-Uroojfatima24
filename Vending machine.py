print('''
░█──░█ ░█▀▀▀ ░█▄─░█ ░█▀▀▄ ▀█▀ ░█▄─░█ ░█▀▀█ 　 ░█▀▄▀█ ─█▀▀█ ░█▀▀█ ░█─░█ ▀█▀ ░█▄─░█ ░█▀▀▀ 
─░█░█─ ░█▀▀▀ ░█░█░█ ░█─░█ ░█─ ░█░█░█ ░█─▄▄ 　 ░█░█░█ ░█▄▄█ ░█─── ░█▀▀█ ░█─ ░█░█░█ ░█▀▀▀ 
──▀▄▀─ ░█▄▄▄ ░█──▀█ ░█▄▄▀ ▄█▄ ░█──▀█ ░█▄▄█ 　 ░█──░█ ░█─░█ ░█▄▄█ ░█─░█ ▄█▄ ░█──▀█ ░█▄▄▄
      ''')
class VendingMachine:
    def __init__(self):
        self.menu = {
            'D1': {'item': 'Cola', 'category': 'Drinks', 'price': 1.50, 'stock': 10},
            'D2': {'item': 'Water', 'category': 'Drinks', 'price': 1.00, 'stock': 15},
            'D3': {'item': 'Mango juice', 'category': 'Drinks', 'price': 2.00, 'stock': 0},
            'D4': {'item': 'Iced coffee', 'category': 'Drinks', 'price': 4.00, 'stock': 6},
            'D5': {'item': 'Iced tea', 'category': 'Drinks', 'price': 3.00, 'stock': 9}, 
            'S1': {'item': 'Chips', 'category': 'Snacks', 'price': 1.25, 'stock': 8},
            'S2': {'item': 'Chocolate', 'category': 'Snacks', 'price': 1.75, 'stock': 12},
            'S3': {'item': 'Cookies', 'category': 'Snacks', 'price': 2.00, 'stock': 4},
            'S4': {'item': 'Popcorn', 'category': 'Snacks', 'price': 2.25, 'stock': 3}, 
            'S5': {'item': 'Croissants', 'category': 'Snacks', 'price': 2.50, 'stock': 7},
        }
        self.balance = 0.0

    def display_menu(self):
        print("Vending Machine Menu:")
        for code, details in self.menu.items():
            print(f"{code}. {details['item']} ({details['category']}) - ${details['price']} - Stock: {details['stock']}")

    def select_item(self):
        code = input("Enter the code of the item you want to purchase: ")
        return self.menu.get(code)

    def insert_money(self):
        amount = float(input("Insert money: $"))
        self.balance += amount

    def calculate_change(self, price):
        change = self.balance - price
        self.balance = 0  # Reset balance after calculating change
        return change

    def dispense_item(self, item):
        print(f"Dispensing {item['item']}... Enjoy your {item['category'].lower()}!")

    def display_change(self, change):
        print(f"Change: ${change:.2f}")

    def buy_additional_item(self):
        choice = input("Do you want to buy an additional item? (yes/no): ")
        return choice.lower() == 'yes'

    def run(self):
        self.display_menu()
        selected_item = self.select_item()

        if selected_item and selected_item['stock'] > 0:
            price = selected_item['price']
            self.insert_money()

            change = self.calculate_change(price)
            if change >= 0:
                selected_item['stock'] -= 1  # Decrease stock
                self.dispense_item(selected_item)
                self.display_change(change)

                if self.buy_additional_item():
                    self.run()
            else:
                print("Insufficient funds. Please insert more money.")
        elif selected_item:
            print("Sorry, the selected item is out of stock.")
        else:
            print("Invalid item code. Please try again.")


if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()