class Store:
    def __init__(self, name, inventory=None):
        self.name = name
        self.inventory = {
            "Juice": {"qty": 8, "price": 2},
            "apples":  {"qty": 24, "price": 0.79},
            "bananas": {"qty": 30, "price": 0.49},
            "bread":   {"qty": 12, "price": 2.99},
            "milk":    {"qty": 8,  "price": 3.49},
            "eggs":    {"qty": 18, "price": 2.79},
            "cheese":  {"qty": 6,  "price": 4.99},
            "lettuce": {"qty": 10, "price": 1.29},
            "yogurt":  {"qty": 20, "price": 0.99},
        }

    def add_item(self):
        item = str(input("Item name: "))
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        self.inventory.update({item: {'qty': qty, 'price': price}})

    def show_inventory(self):
        print(f"--- {self.name}'s inventory ---")
        print(f"{'Item':<12} {'Qty':>6} {'Price':>8}")
        print("-" * 29)
    
        for item, data in self.inventory.items():
            price_str = f"${data['price']:.2f}"
            print(f"{item.title():<12} {data['qty']:>5}  {price_str:>8}")


class Shopper:
    def __init__(self, name, balance, store, cart=None):
        self.name = name
        self.balance = balance
        self.store = store
        self.cart = {}
    
    def add_to_cart(self):
        item = str(input("What item do you want to add to your cart? "))


shaws = Store("Shaws")
john = Shopper("John", 50)

#shaws.show_inventory()
#shaws.add_item()
#shaws.show_inventory()
john.add_to_cart()
