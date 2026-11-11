text = input("Enter a text: ").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}
characters = set(text) # use to remove duplicates
unique_vowels = characters & vowels # intersection of characters and vowels
print("Unique vowels in the text:", sorted(unique_vowels))