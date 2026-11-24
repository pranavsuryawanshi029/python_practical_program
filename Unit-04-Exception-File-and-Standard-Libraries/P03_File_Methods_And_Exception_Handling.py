
file = None

try:
    # Open existing file
    file = open("student.txt", "r")

    # Display file name and mode
    print("File Name:", file.name)
    print("File Mode:", file.mode)

    # Using tell()
    print("File Position:", file.tell())

    # Using readline()
    print("\nFirst Line:")
    print(file.readline(), end="")

    # Using seek()
    file.seek(0)

    # Using readlines()
    print("\n\nAll Lines:")
    print("".join(file.readlines()))

    # Using read()
    file.seek(0)
    print("Complete File Content:")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

else:
    print("\nFile read successfully.")

finally:
    if file is not None:
        file.close()
        print("File closed successfully.")