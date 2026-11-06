name = input("Enter student name: ")
status = input("Enter attendance status (Present/Absent): ")

with open("attendance.txt", "a") as file:
    file.write(f"Student Name: {name}, Attendance: {status}\n")

print("Attendance recorded successfully.")