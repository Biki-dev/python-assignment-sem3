text = input("Enter a paragraph: ").lower()
text = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
        
for frequency_word, count in frequency.items():
    print(f"{frequency_word}: {count}")