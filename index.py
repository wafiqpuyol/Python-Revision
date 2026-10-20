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