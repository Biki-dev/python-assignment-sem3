import math

H = float(input("Enter tank height: "))
L = float(input("Enter tank length: "))
B = float(input("Enter tank breadth: "))

h = float(input("Enter glass height: "))
r = float(input("Enter glass radius: "))

if H <= 0 or L <= 0 or B <= 0 or h <= 0 or r <= 0:
    print("All dimensions must be positive")
else:
    tank_volume = H * L * B
    glass_volume = math.pi * r * r * h
    total_glasses = int(tank_volume / glass_volume)

    print("Tank Volume:", tank_volume)
    print("Glass Volume:", glass_volume)
    print("Number of Full Glasses:", total_glasses)