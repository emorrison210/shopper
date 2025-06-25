class Store:
    def __init__(self, name, inventory=None):
        self.name = name
        self.inventory = {
            "juice": {"qty": 8, "price": 2},
            "apples":  {"qty": 24, "price": 0.79},
            "bananas": {"qty": 30, "price": 0.49},
            "bread":   {"qty": 12, "price": 2.99},
            "milk":    {"qty": 8,  "price": 3.49},
            "eggs":    {"qty": 18, "price": 2.79},
            "cheese":  {"qty": 6,  "price": 4.99},
            "lettuce": {"qty": 10, "price": 1.29},
            "yogurt":  {"qty": 20, "price": 0.99},
        }

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
        return (f"{self.name} has ${self.balance} and is shopping at {self.store.name}\n{self.cart}")
        
    # add items from store to cart
    def add_to_cart(self):
        self.store.show_inventory()
        item = str(input("What item do you want to add to your cart? ")).lower()
        
        if item not in self.store.inventory:
            print("That item is not sold here.")
            return # exits early
        
        stock = self.store.inventory[item]['qty']
        price = self.store.inventory[item]['price']
        print(f"{item} costs ${price}")
        
        qty = int(input("How many do you want? "))
        
        if qty <= stock:
            self.cart.update({item: qty})
            self.balance -= self.store.inventory[item]['price'] * qty
        
        elif qty > stock:
            print('Error. Can''t buy more than the shop has.')
            
            
shaws = Store("Shaws")
john = Shopper("John", 50, shaws)

#shaws.show_inventory()
#shaws.add_item()
#shaws.show_inventory()
john.add_to_cart()
print(john)
