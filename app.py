print("Hello World")

String1 = 'Welcome to the Geeks World'
String2 = 'Welcome to the\n Geeks World' # \n adds a new line to the string.
print("Strings with the use of Single Quotes: ")
print(String1)
print(String2)

print(String1.upper()) #ALL CAPS
print(String1.lower()) #lowercase
print(String1.isupper()) #True/False if string is all uppercase
print(String1.islower()) #True/False if string is all lowercase

print(String1.casefold()) #lowercase
print(String1.capitalize()) #First letter Captial
print(String1.swapcase()) #letter casing swaps
print(String1.__repr__())
print(String1.__str__())

print(String1 + " ,This is cool!") #Appending a string onto another string "Concantenation"

print(len(String1))

print(String1[5])

print(String1.index("G"))
print(String1.index("Geeks"))

print(String1.replace("World", "Universe")) #Replace words or letters in strings


