import os

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.quantity} units @ ${self.price:.2f} each"

class InventoryManager:
    FILE_PATH = "inventory.txt"

    def __init__(self):
        self.items = []
        self.load_from_file()

    def add_item(self):
        name = input("Enter item name: ").strip()
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit (in dollars): "))
            if quantity <= 0 or price <= 0:
                print("Quantity and price must be positive numbers.")
                return
            self.items.append(InventoryItem(name, quantity, price))
            self.save_to_file()
            print("Item added successfully!")
        except ValueError:
            print("Invalid input. Quantity and price must be numbers.")

    def view_inventory(self):
        print("\n=== Inventory ===")
        if not self.items:
            print("No items in inventory.")
            return
        for item in self.items:
            print(item)

    def remove_item(self):
        name = input("Enter the name of the item to remove: ").strip()
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                self.save_to_file()
                print("Item removed successfully!")
                return
        print("Item not found.")

    def adjust_quantity(self):
        name = input("Enter the name of the item to adjust quantity: ").strip()
        for item in self.items:
            if item.name.lower() == name.lower():
                try:
                    adjustment = int(input("Enter quantity adjustment (negative to decrease): "))
                    new_quantity = item.quantity + adjustment
                    if new_quantity < 0:
                        print("Quantity cannot be negative.")
                        return
                    item.quantity = new_quantity
                    self.save_to_file()
                    print(f"Updated quantity for {item.name}: {item.quantity} units.")
                except ValueError:
                    print("Invalid input. Adjustment must be a number.")
                return
        print("Item not found.")

    def change_price(self):
        name = input("Enter the name of the item to change price: ").strip()
        for item in self.items:
            if item.name.lower() == name.lower():
                try:
                    new_price = float(input("Enter new price: "))
                    if new_price <= 0:
                        print("Price must be a positive number.")
                        return
                    item.price = new_price
                    self.save_to_file()
                    print(f"Updated price for {item.name}: ${item.price:.2f}.")
                except ValueError:
                    print("Invalid input. Price must be a number.")
                return
        print("Item not found.")

    def save_to_file(self):
        with open(self.FILE_PATH, "w") as file:
            for item in self.items:
                file.write(f"{item.name}|{item.quantity}|{item.price}\n")

    def load_from_file(self):
        if not os.path.exists(self.FILE_PATH):
            return
        with open(self.FILE_PATH, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    try:
                        name = parts[0]
                        quantity = int(parts[1])
                        price = float(parts[2])
                        self.items.append(InventoryItem(name, quantity, price))
                    except ValueError:
                        print(f"Skipping invalid line in file: {line.strip()}")

def main():
    manager = InventoryManager()
    while True:
        print("\n=== Inventory Manager ===")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Remove Item")
        print("4. Adjust Quantity")
        print("5. Change Price")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            manager.add_item()
        elif choice == "2":
            manager.view_inventory()
        elif choice == "3":
            manager.remove_item()
        elif choice == "4":
            manager.adjust_quantity()
        elif choice == "5":
            manager.change_price()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
