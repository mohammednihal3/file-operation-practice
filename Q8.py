with open("students.txt", "w") as file:
    for i in range(5):
        name = input("Enter student name: ")
        file.write(name + "\n")

print("Student names saved successfully.")
