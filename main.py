class Store:
    def __init__(self, name, inventoryDict):
        self.name = name
        self.inventory = inventoryDict

    # add an item to the store inventory
    def add_item(self):
        item = str(input("Item name: "))
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        self.inventory.update({item: {'qty': qty, 'price': price}})

    # prints out the store inventory
    def show_inventory(self):
        print(f"--- {self.name}'s inventory ---")
        print(f"{'Item':<12} {'Qty':>6} {'Price':>8}")
        print("-" * 29)
    
    # for each item in the inventory print out the corresponding qty and price
        for item, data in self.inventory.items():
            price_str = f"${data['price']:.2f}"
            print(f"{item.title():<12} {data['qty']:>5}  {price_str:>8}")


class Shopper:
    def __init__(self, name, balance, store, cart=None):
        self.name = name
        self.balance = balance
        self.store = store
        self.cart = cart or {}
    
    def __repr__(self):
        return (f"{self.name} has ${self.balance} and is shopping at {self.store.name}")
        
    # add items from store to cart
    def add_to_cart(self):
        while True:
            self.store.show_inventory()
            item = str(input("Enter an item to add to your cart or type none to exit: ")).lower()
            
            if item == "none":
                break
            
            if item not in self.store.inventory:
                print("That item is not sold here.")
                continue
        
            stock = self.store.inventory[item]['qty']
            price = self.store.inventory[item]['price']
            print(f"{item} costs ${price}")

            qty = int(input("How many do you want? "))
        
            if qty <= stock:
                self.cart[item] = self.cart.get(item, 0) + qty
                self.balance -= price * qty
                self.store.inventory[item]['qty'] -= qty
        
            elif qty > stock:
                print('Error. Can''t buy more than the shop has.')
        
            print(f"You now have ${self.balance} left")
    
    def print_shopper(self):
        print(f"You have ${self.balance} left")
        for item, data in self.cart.items():
            print(f"{item.title()}: {data}\n")

shaws_inventory = {
            "juice":   {"qty": 8, "price": 2},
            "apples":  {"qty": 24, "price": 0.79},
            "bananas": {"qty": 30, "price": 0.49},
            "bread":   {"qty": 12, "price": 2.99},
            "milk":    {"qty": 8,  "price": 3.49},
            "eggs":    {"qty": 18, "price": 2.79},
            "cheese":  {"qty": 6,  "price": 4.99},
            "lettuce": {"qty": 10, "price": 1.29},
            "yogurt":  {"qty": 20, "price": 0.99},
        }

corner_market_inventory = {
    "apple": {"price": 0.5, "qty": 30},
    "banana": {"price": 0.3, "qty": 50},
    "bread": {"price": 2.0, "qty": 20},
    "milk": {"price": 1.5, "qty": 15},
    "eggs": {"price": 3.0, "qty": 12},
    "cheese": {"price": 4.5, "qty": 10},
    "chicken": {"price": 7.0, "qty": 8},
    "rice": {"price": 1.2, "qty": 25},
    "pasta": {"price": 1.0, "qty": 18},
    "carrot": {"price": 0.2, "qty": 40}
}

bobs_market_inventory = {
    "orange": {"price": 0.6, "qty": 35},
    "grapes": {"price": 2.5, "qty": 15},
    "yogurt": {"price": 1.0, "qty": 20},
    "butter": {"price": 3.2, "qty": 10},
    "cereal": {"price": 3.8, "qty": 12},
    "beef": {"price": 8.5, "qty": 7},
    "lettuce": {"price": 1.1, "qty": 25},
    "tomato": {"price": 0.4, "qty": 30},
    "onion": {"price": 0.3, "qty": 45},
    "juice": {"price": 2.6, "qty": 18}
}

# Runs the app
def main():
    name = str(input("Enter your name: "))
    balance = float(input("How much money do you have? "))
    choice = int(input("Which store do you want to shop at?\n1. Shaws\n2. Corner Market\n3. Bobs Groceries\n"))
    
    if choice == 1:
        store = Store("Shaws", shaws_inventory)
    elif choice == 2:
        store = Store("Corner Market", corner_market_inventory)
    elif choice == 3:
        store = Store("Bob's Market", bobs_market_inventory)
    else:
        print("Error. Make sure to enter in a number from 1-3")
    
    customer = Shopper(name, balance, store)
    customer.add_to_cart()
    customer.print_shopper()
    
    
main()


# example commands
'''
shaws = Store("Shaws", shaws_inventory)
john = Shopper("John", 50, shaws)
print(john)
john.add_to_cart()
john.print_shopper()
shaws.add_item()
'''