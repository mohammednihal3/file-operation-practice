word = input("Enter the word to count: ")

with open("student.txt", "r") as file:
    content = file.read()

    count = content.lower().split().count(word.lower())

print("The word", word, "occurs", count, "times in the file.")