n = int(input("Enter a number: "))
grid = [[0 for j in range(n)] for i in range(n)]

num = 1
top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        grid[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        grid[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            grid[bottom][i] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            grid[i][left] = num
            num += 1
        left += 1

for row in grid:
    print(" ".join(map(str, row)))