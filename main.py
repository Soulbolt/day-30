# TRY CATCH EXCEPTION ERRORS IN PYTHON

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:
    file = open("a_file.txt")  # Attempt to open file if it exist.
    a_dictionary = {"key": "value"}  # Dictionary with one key value pair
    print(a_dictionary["sadad"])  # Attemping to access an non existing key.
except FileNotFoundError:
    file = open("a_file.txt", "w")  # If file does not exist, create one.
    file.write("something")  # Write something to the file
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")  # If key does not exist, print error message
else:
    content = file.read()  # If file exist, read and print its contents.
    print(content)
finally:
    file.close()  # Close the file.
    print("File was closed.")
    # We can purposely raise an error with: raise TypeError("this is an error that I made up.") Example below

height = float("Height: ")
weight = int("Weight: ")
if height > 3:
    raise ValueError("human height shouild not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)
