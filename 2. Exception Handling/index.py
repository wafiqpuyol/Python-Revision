# Handling File Exception
import os

print("Try except block started.")
try :

    folder_name = "temp"
    file_name = "temp_4.txt"
    num = 1

    file_path = os.path.join(folder_name, file_name)
    f = open(file_path, "r+")
    contents = f.read()
    print(contents)

    cal = 100 / num
    print(cal)

except FileNotFoundError:
    print("File not found,Please check correct file name or path")
    print("Current location is : ", os.getcwd())
    print("Files present in current directory : ", os.listdir(os.path.join(os.getcwd(), folder_name)))
    print("File name selected : ", "temp/temp_3.txt")
except TypeError:
    print("Issue with multiple type operation.")
except Exception as e:
    print("Caught in parent exception", e)
else :
    print("try block successfully execute.")
finally :
    try :
        f.close()
        print("File is closed.")
    except NameError:
        print("File was never initialised.")
print("Try except block completed.")


# Handling the exception event through parent Exception
try:
  num = 0
  cal = 100 / num
  print(cal)
except Exception as e:
  print("Caught in parent exception: ", e)
 

# Handling the exact exception event
try:
  num = 0
  cal = 100 / num
  print(cal)
except ZeroDivisionError as z:
  print("Issue with arithmetic operation: ", z)
except Exception as e:
  print("Caught in parent exception: ", e)
