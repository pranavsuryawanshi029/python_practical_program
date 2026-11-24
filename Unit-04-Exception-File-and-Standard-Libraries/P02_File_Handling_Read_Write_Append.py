
# Write student details into file
file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
student_class = input("Enter class: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Class: " + student_class + "\n")

file.close()

# Read complete file
file = open("student.txt", "r")

print("\n--- Student Details ---")
print(file.read())

file.close()

# Append additional student details
file = open("student.txt", "a")

name = input("Enter another student name: ")
roll = input("Enter roll number: ")
student_class = input("Enter class: ")

file.write("\nName: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Class: " + student_class + "\n")

file.close()

# Read file line by line
file = open("student.txt", "r")

print("\n--- All Student Records ---")

for line in file:
    print(line, end="")

file.close()