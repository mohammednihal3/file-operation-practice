word = input("Enter the word to search: ")

with open("student.txt", "r") as file:
    content = file.read()

    if word.lower() in content.lower():
        print("Word found in the file.")
    else:
        print("Word not found in the file.")