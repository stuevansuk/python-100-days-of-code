# CMD + / to comment lines
# #Simnple Printing
print("Day 1 - Python Printing Function")
print("The Function is declared like this:")

#Printing with "" in Strings
print("print('what to print')")
print('print("what to print")')

#Printing on New Lines
print("Hello World!\nHello World")
print("Hello\nMy Name Is\nStuart Evans")

#String Concatenation
print("Hello" + "Stuart")
print("Hello" +  " Stuart")
print("Hello" + " " + "Stuart")

#Fixing Broken Code 
print("Day 1 - String Manipulation")
print("String Concatenation is done with the" + ' + ' + "sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and \n")

# #Input Functions
#input() will get the user input from the console
#print() will print the word Hello and the user input in one string.
input("What is you name?\n")
print("Hello " + input("What is your name?\n"))

# Write a program that prints the number of characters in a user's name.
# len() will calcuate the length of a string.
# print() will print the value of the length of the string
name = input("Hello what is your name?\n")
print(len(name))

#Less efficient way of doing it, nesting the funtions!
print(len(input("What is your name?\n")))

# Adding more variables 
name = input("Hello what is your name?\n")
length = len(name)
print(name)

#Basic variables
name = input("What is your name?")
print(name)

#Sets the variable
name = "Jack"
print(name)

#Code Challenge: Write a program that switches the values stored in the variables a and b.
a = input("a:")
b = input("b:")
print("a=", b)
print("b=", a)

#Actually switch the content of the variables to anotehr placehorlder variable, like moving liquid around containers
a = input("a:")
b = input("b:")
c = a
a = b
b = c
print("a : " + a)
print("b : " + b)

#1. Create a greeting for your program.
print("\n-----Welcome to the Band Name Generator------\n")
#2. Ask the user for the city that they grew up in.
city = input("Q. Let me know what City you Grew Up in\n")
#3. Ask the user for the name of a pet.
pet = input("Q. Let me know what you pet was called.\n")
#4. Combine the name of their city and pet and show them their band name.
print("You band name is : " + city + " " + pet)
placeholder = city
city = pet 
pet = placeholder
print("Or how about?: " + city + " " + pet)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end