student_id = int(input("Enter Student ID: "))
name = input("Enter Student Name: ")
grade = input("Enter Grade: ")
math_score = float(input("Enter Math Score: "))
physics_score = float(input("Enter Physics Score: "))

student = (student_id, name, grade, (math_score, physics_score))

student_id, name, grade, (math_score, physics_score) = student

print("\n----- Student Summary -----")
print(f"Student ID: {student_id}")
print(f"Name: {name}")
print(f"Grade: {grade}")
print(f"Math Score: {math_score}")
print(f"Physics Score: {physics_score}")