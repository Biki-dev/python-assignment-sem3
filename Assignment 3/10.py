items = [("Apple", 50), ("Banana", 20), ("Cherry", 75)]
items.sort(key=lambda x: x[1], reverse=True)
# key=lambda x: x[1] => Sort using the second element (price)
print(items)