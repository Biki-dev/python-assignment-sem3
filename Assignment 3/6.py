m = int(input("Enter number of rows count: "))
n = int(input("Enter number of columns count: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        num = int(input(f"Enter number for row {i + 1}, column {j + 1}: "))
        row.append(num)
    matrix.append(row)

print("The matrix you entered is:")

for row in matrix:
    print(row)
    
transpose = []

for j in range(n):
    col = []
    for i in range(m):
        col.append(matrix[i][j])
    transpose.append(col)

print("The transpose of the matrix is:")

for row in transpose:
    print(row)