x1, y1 = map(int, input("Enter Bottom-Left Values (x1,y1): ").split())
x2, y2 = map(int, input("Enter Top-Right Values (x2,y2): ").split())
x, y = map(int, input("Enter User Point Values (x,y): ").split())

if x1 < x < x2 and y1 < y < y2:
    print("The point is inside the rectangle.")
elif x1 <= x <= x2 and y1 <= y <= y2:
    print("The point is on the rectangle.")
else:
    print("The point is outside the rectangle.")