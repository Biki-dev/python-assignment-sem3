elements = [3, 1, 2]
power_set = [[]]


for element in elements:
    new_subsets = []

    for subset in power_set:
        new_subset = subset.copy()
        new_subset.append(element)
        new_subsets.append(new_subset)

    power_set.extend(new_subsets)

print("Elements Used: ", elements)
print("The power set: ", power_set)
