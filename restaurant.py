

class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} : ₹{self.price}"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        print("\nMenu:")
        categories = {}
        for item in self.items:
            if item.category not in categories:
                categories[item.category] = []
            categories[item.category].append(item)

        for category, items in categories.items():
            print(f"\n{category}:\n" + "=" * len(category))
            i_n = 1
            for item in items:
                print(f"{i_n}.{item}")
                i_n += 1
                

class Order:
    def __init__(self):
        self.items = []  # Changed to a simple list to store items

    def add_item(self, item):
        self.items.append(item)  # Add item directly to the list

    def calculate_total(self):
        return sum(item.price for item in self.items)  # Calculate total without quantity

    def display_order(self):
        print("\nYour Order:")
        for item in self.items:
            print(f"{item}")
        print(f"\nTotal bill: ₹{self.calculate_total()}")
        print("\nThank you for coming, please visit again!\n")


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()

    def take_order(self):
        order = Order()
        while True:
            self.menu.display_menu()
            choice = input("Enter the name of the item you want to order (type 'stop' to finish your order): ")
            if choice.lower() == "stop":
                break
            for item in self.menu.items:
                if item.name.lower() == choice.lower():
                    order.add_item(item)
                    print(f"Added {item.name} to your order.")
                    break
            else:
                print("Item not found. Please try again.")
        return order



# Example Execution
restaurant = Restaurant("Foodies Home")
restaurant.menu.add_item(MenuItem("Fried Rice", 10.12, "Main Course"))
restaurant.menu.add_item(MenuItem("Sirlion Steak", 11.48, "Main Course"))
restaurant.menu.add_item(MenuItem("Spicy Chicken", 12.14, "Main Course"))
restaurant.menu.add_item(MenuItem("Grilled Salmon Fish", 13, "Main Course"))
restaurant.menu.add_item(MenuItem("Deep Bake Goose", 14.22, "Main Course"))
restaurant.menu.add_item(MenuItem("Avocado Toast", 10, "Appetizers"))
restaurant.menu.add_item(MenuItem("Spaghetti Pasta", 10.99, "Appetizers"))
restaurant.menu.add_item(MenuItem("Chicken Pie", 12.40, "Appetizers"))
restaurant.menu.add_item(MenuItem("Fish Sandwich", 13.02, "Appetizers"))
restaurant.menu.add_item(MenuItem("Vegetable Salad", 9.88, "Appetizers"))
restaurant.menu.add_item(MenuItem("Water", 2, "Drinks"))
restaurant.menu.add_item(MenuItem("Jasmine Tea", 4.56, "Drinks"))
restaurant.menu.add_item(MenuItem("Lemonade", 5, "Drinks"))
restaurant.menu.add_item(MenuItem("Fresh Juice", 5, "Drinks"))
restaurant.menu.add_item(MenuItem("Smoothie", 5.42, "Drinks"))
restaurant.menu.add_item(MenuItem("Indian Pasta", 13.76, "Main Course"))

print(f"Welcome to {restaurant.name}!")
order = restaurant.take_order()
order.display_order()
