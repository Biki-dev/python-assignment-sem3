text = input("Enter a text: ").lower()
alphabet = set("abcdefghijklmnopqrstuvwxyz")
characters = set(text)
intersection = sorted(characters & alphabet)
if intersection == sorted(alphabet):
    print("The text is Pangram.")
else:
    print("The text is not Pangram.")