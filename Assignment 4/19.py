class Matrix:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value
    def __iter__(self):
        return iter(self.data)
matrix = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Original Matrix:")
for row in matrix:
    print(row)
print("Number of Rows:", len(matrix))
print("Element at [0][1]:", matrix[0][1])
matrix[1][2] = 99
print("\nUpdated Matrix:")
for row in matrix:
    print(row)
matrix[0] = [10, 20, 30]
print("\nAfter Updating First Row:")
for row in matrix:
    print(row)