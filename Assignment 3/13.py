codingClub = ["Biki", "Rohit", "Saurabh", "Ankit", "Amit", "Rohit"]
isteClub = ["Mrinal", "Ram", "Rohit", "Ankit", "Biki", "Madhurja"]

result = list(set(codingClub) ^ set(isteClub)) # symmetric difference
print("Members in either club but not both:", result)