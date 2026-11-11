inventory1 = {'Apples': 10, 'Oranges': 5}
inventory2 = {'Oranges': 8, 'Bananas': 12}

merged_inventory = {}

for key, value in inventory1.items():
    merged_inventory[key] = value
for key, value in inventory2.items():
    if key in merged_inventory:
        merged_inventory[key] += value
    else:
        merged_inventory[key] = value

print("Merged Inventory: ", merged_inventory)