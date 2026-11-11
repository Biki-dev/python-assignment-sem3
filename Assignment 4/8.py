def hanoi(n, source, target, auxiliary):
    if n == 0:
        return 0
    moves = hanoi(n - 1, source, auxiliary, target)
    print("Move disk", n, "from", source, "to", target)
    moves += 1
    moves += hanoi(n - 1, auxiliary, target, source)
    return moves

n = 3
total_moves = hanoi(n, 'A', 'C', 'B')
print("\nTotal number of moves:", total_moves)