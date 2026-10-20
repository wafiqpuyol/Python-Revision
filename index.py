try:
    with open('temp/dummy.txt', 'r+', encoding='utf-8') as file:
        file.read()
        data = file.write("Wafiq hossain")
        print(data)
except FileNotFoundError:
        print("Error: The file or directory could not be found.")
except UnicodeDecodeError:
        print("Error: Failed to decode the file with UTF-8 encoding.")