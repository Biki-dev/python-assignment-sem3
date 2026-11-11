def generate_permutations(s):
    result = []

    def backtrack(current, remaining):
        if len(remaining) == 0:
            result.append(current)
            return
        used = set()
        for i in range(len(remaining)):
            char = remaining[i]
            if char in used:
                continue
            used.add(char)
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(current + char, new_remaining)
    backtrack("", s)
    return result


string = "AAB"
permutations = generate_permutations(string)
print("Original String:", string) # AAB
print("Unique Permutations:", permutations) # ['AAB', 'ABA', 'BAA']
print("Total Permutations:", len(permutations)) # 3
