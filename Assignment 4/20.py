from abc import ABC, abstractmethod
class Item:
    def __init__(self, item_id, name, price, stock_quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
class Discount(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass
class PercentageDiscount(Discount):
    def __init__(self, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("Invalid discount percentage")
        self.percentage = percentage
    def apply_discount(self, total):
        return total - (total * self.percentage / 100)
class FlatDiscount(Discount):
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Discount cannot be negative")
        self.amount = amount
    def apply_discount(self, total):
        return max(0, total - self.amount)
class ShoppingCart:
    def __init__(self, discount=None):
        self.items = {}
        self.discount = discount
    def add_item(self, item, quantity=1):
        if quantity <= 0:
            print("Quantity must be positive")
            return
        if quantity > item.stock_quantity:
            print("Insufficient stock for", item.name)
            return
        if item.item_id in self.items:
            if self.items[item.item_id]["item"] is not item:
                print("Item ID already exists")
                return
            self.items[item.item_id]["quantity"] += quantity
        else:
            self.items[item.item_id] = {"item": item, "quantity": quantity}
        item.stock_quantity -= quantity
        print(quantity, item.name, "added to cart")
    def remove_item(self, item_id, quantity=1):
        if item_id not in self.items:
            print("Item not found in cart")
            return
        if quantity <= 0:
            print("Quantity must be positive")
            return
        entry = self.items[item_id]
        if quantity > entry["quantity"]:
            print("Not enough quantity in cart")
            return
        entry["quantity"] -= quantity
        entry["item"].stock_quantity += quantity
        if entry["quantity"] == 0:
            del self.items[item_id]
        print(quantity, "item(s) removed from cart")
    def compute_total(self):
        subtotal = 0
        for entry in self.items.values():
            subtotal += entry["item"].price * entry["quantity"]
        if self.discount:
            return self.discount.apply_discount(subtotal)
        return subtotal
item1 = Item("I101", "Keyboard", 1500, 10)
item2 = Item("I102", "Mouse", 500, 5)
discount = PercentageDiscount(10)
cart = ShoppingCart(discount)
cart.add_item(item1, 2)
cart.add_item(item2, 1)
print("\nShopping Cart:")
for entry in cart.items.values():
    item = entry["item"]
    print(item.name, "| Price:", item.price, "| Quantity:", entry["quantity"])
print("\nTotal Amount:", cart.compute_total())
cart.remove_item("I102", 1)
print("\nAfter Removing Mouse:")
print("Total Amount:", cart.compute_total())
print("Remaining Keyboard Stock:", item1.stock_quantity)
print("Remaining Mouse Stock:", item2.stock_quantity)