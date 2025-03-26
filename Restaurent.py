
"""
#    Restaurant Management Python (oops)
   =========================================
"""


class MenuItems:

    def __init__(self,item_name,price,category):
        self.item_name=item_name                  # menu - item_name 
        self.price=price
        self.category=category

    def __str__(self):
        return f"{self.item_name} : ${self.price}"        # <__main__at 0x000002BE00F76630>  == hexadecimal id of object
    
class Menu:                  # of class: MenuItem

    def __init__(self):
        self.items=[]        # items-list

    def add_item(self,item):
        self.items.append(item)

    def display(self):
        print("\nMenu:\n")
        categories = {}
        for item in self.items:
            if item.category not in categories:
                categories[item.category] = []
            categories[item.category].append(item)

        for category , items in categories.items():
            print(f"{category}: \n{"="*len(category)} ")
            item_number = 1
            for item in items:
                print(f"{item_number}. {item}")
                item_number += 1

class Order:

    def __init__(self):
        self.items_order= {}   # to store items respect their quantities

    def add_order(self, item, quantity):
        if item in self.items_order:
            self.items_order[item] += quantity    # Increase quantity if item already added
        else:
            self.items_order[item] = quantity

    def calculate_total(self):
        return sum(item.price * quantity for item, quantity in self.items_order.items())
    
    def display_order(self):
        print("\nYour order:")
        for item , quantity in self.items_order.items():
            print(f"{item.item_name} x {quantity} : {item.price * quantity}")
        print(f"Your Total bill: {self.calculate_total()}")
        print("\nThank you for coming! Please visit Again!!")


class Restaurant:         # main class which coordinate menu and order

    def __init__(self,name): # restaurant name
        self.name=name
        self.menu=Menu()

    def menu_order(self):
        order = Order()
        while True:
            self.menu.display()
            choice = input("what would you like to order (press 'enter' to finish your order)? --> ")
            if choice.lower() == '':
                break
            for item in self.menu.items:
                if item.item_name.lower() == choice.lower():
                    while True:
                        try:
                            quantity = int(input(f"How many {item.item_name} would you like to order? "))
                            if quantity > 0:
                                order.add_order(item,quantity)
                                print(f"Added {item.item_name} to your order.")
                                break
                            else:
                                print("Please enter a positive no:")
                        except ValueError:
                            print("Invalid input. Please enter a no:")
                    break
            else:
                print("Item not found")

        return order



restaurant = Restaurant("Foodies Home")
restaurant.menu.add_item(MenuItems("Fried Rice", 10.12, "Main Course"))
restaurant.menu.add_item(MenuItems("Sirlion Steak", 11.48, "Main Course"))
restaurant.menu.add_item(MenuItems("Spicy Chicken", 12.14, "Main Course"))
restaurant.menu.add_item(MenuItems("Grilled Salmon Fish", 13, "Main Course"))
restaurant.menu.add_item(MenuItems("Deep Bake Goose", 14.22, "Main Course"))
restaurant.menu.add_item(MenuItems("Avocado Toast", 10, "Appetizers"))
restaurant.menu.add_item(MenuItems("Spaghetti Pasta", 10.99, "Appetizers"))
restaurant.menu.add_item(MenuItems("Chicken Pie", 12.40, "Appetizers"))
restaurant.menu.add_item(MenuItems("Fish Sandwich", 13.02, "Appetizers"))
restaurant.menu.add_item(MenuItems("Vegetable Salad", 9.88, "Appetizers"))
restaurant.menu.add_item(MenuItems("Water", 2, "Drinks"))
restaurant.menu.add_item(MenuItems("Jasmine Tea", 4.56, "Drinks"))
restaurant.menu.add_item(MenuItems("Lemonade", 5, "Drinks"))
restaurant.menu.add_item(MenuItems("Fresh Juice", 5, "Drinks"))
restaurant.menu.add_item(MenuItems("Smoothie", 5.42, "Drinks"))
restaurant.menu.add_item(MenuItems("Indian Pasta", 13.76, "Main Course"))

print(f"\nWelcome to {restaurant.name}!!\n")
order = restaurant.menu_order()
order.display_order()

