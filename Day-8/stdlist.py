# Taking number of students
n = int(input("Enter the number of students: "))

names = []
cgpas = []

# Taking inputs
for i in range(n):
    print(f"\n----------- Student {i + 1} -----------")
    name = input("Enter the name: ")
    cgpa = float(input("Enter the CGPA: "))

    names.append(name)
    cgpas.append(cgpa)

# Display all students
print("\nName".ljust(15), "CGPA")
print("-" * 22)

for i in range(n):
    print(names[i].ljust(15), cgpas[i])

# Finding maximum and minimum CGPA
max_cgpa = max(cgpas)
min_cgpa = min(cgpas)

max_index = cgpas.index(max_cgpa)
min_index = cgpas.index(min_cgpa)

# Display results
print("\nHighest CGPA:")
print(f"Name: {names[max_index]}, CGPA: {max_cgpa}")

print("\nLowest CGPA:")
print(f"Name: {names[min_index]}, CGPA: {min_cgpa}")
