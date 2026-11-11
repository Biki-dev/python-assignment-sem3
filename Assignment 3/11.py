employees = [
    ("Xor", 35, "IT", 50000),
    ("Roki", 25, "HR", 30000),
    ("Damit", 32, "IT", 60000),
    ("Ayna", 40, "Finance", 55000)
]

result = []

for employee in employees:
    name, age, department, salary = employee
    if department == "IT" and age > 30:
        result.append((name, age, department, salary))
        
result = tuple(result)

print(result)