# Function
def calculate_bill(customer_name, *args, **kwargs):
    subtotal = 0
    for price in args:
        subtotal += price
    
    discount = kwargs.get('discount', 0)
    tax = kwargs.get('tax', 0)
    
    discount_amount = subtotal * discount/100
    after_discount = subtotal - discount_amount
    
    tax_amount = after_discount * tax/100
    net_total = after_discount + tax_amount
    
    return customer_name, args, subtotal, discount_amount, tax_amount, net_total


# call function and print
bill = calculate_bill(
    "Biki",
    100, 200, 300,
    discount=10,
    tax=5
)
customer, items, subtotal, discount, tax, net_total = bill

print(f"Customer Name : {customer}")
for i, price in enumerate(items, start=1):
    print(f"Item {i}         : ₹{price:.2f}")
print(f"Subtotal      : ₹{subtotal:.2f}")
print(f"Discount      : -₹{discount:.2f}")
print(f"Tax           : +₹{tax:.2f}")
print(f"NET TOTAL     : ₹{net_total:.2f}")