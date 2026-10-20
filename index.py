# Reading & Writing
try:
    with open('temp/dummy.txt', 'r+', encoding='utf-8') as file:
        file.read()
        data = file.write("Wafiq hossain")
        print(data)
except FileNotFoundError:
        print("Error: The file or directory could not be found.")
except UnicodeDecodeError:
        print("Error: Failed to decode the file with UTF-8 encoding.")


# Append + Read
try:
    with open('temp/dummy.txt', 'a+', encoding='utf-8') as file:
        file.write(" Hossain") # Appends the string to the end of the file
        file.seek(0) #Moves the cursor to the start of the file to read the entire content
        print(file.read()) 
except FileNotFoundError:
        print("Error: The file or directory could not be found.")
except UnicodeDecodeError:
        print("Error: Failed to decode the file with UTF-8 encoding.")


# Writing & Reading
try:
    with open('temp/dummy.txt', 'w+', encoding='utf-8') as file:
        print(file.tell())     #points to the 0th index
        print(file.read())     #nothing will print
        file.write("hossain")  #wipe out the existing content then write this
        print(file.tell())     #points to the last index still nothing will print
except FileNotFoundError:
        print("Error: The file or directory could not be found.")
except UnicodeDecodeError:
        print("Error: Failed to decode the file with UTF-8 encoding.")



# Write in a specific position without overwriting existing contents
try:
    with open('temp/dummy.txt', 'r+', encoding='utf-8') as file:
        file.read()             #moving the pointer at the end
        file.write(" hossain")  #append it
        print(file.seek(1))     #moves the pointer
        file.write("I")         #overwrite the existing positioned content with the lastest one
        print(file.tell())     #points to the last index still nothing will print
except FileNotFoundError:
        print("Error: The file or directory could not be found.")
except UnicodeDecodeError:
        print("Error: Failed to decode the file with UTF-8 encoding.")