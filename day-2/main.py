#Data Types

#String Data Type, Print Character of String using [] Subscripting
# print("Hello"[4])
# print("123") 

#Integer - Use _ to make number eeasier readable in code, program will drop them
# print(123 + 345)
# print(123_456_789)

#Float number with decimal point 3.142

#Boolean, are either True or Fale

#Converting Data Types
# num_char = len(input("what is you name? : "))
# str_num_char = str(num_char)
# print("Your name has " + str_num_char + " characters!")

#Prints Type will be a float
# a = 123
# print(type(a))

#Prints Type, will be a string
# a = str(123)
# print(type(a))

#Prints type, will be a float
# a = float(123)
# print(type(a))

# Will print the addition of 70 + 100.5 becuase these are int and flots
# print (70 +float(100.5))

#Will print 70100 as this is defining numbers as a string
# print (str(79) + str(100))

#Challenge 
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#Example input = 39 Exmple output 3 + 9 = 12

# num_1 = int(input("Number 1 : "))
# num_2 = int(input("Number 2 : "))
# print(num_1 + num_2)

# two_digit_number = input("Provide a 2 Digit Number : ")
# number_1 = int(two_digit_number[0]) # Gets 1st Character of the String and sets it as an integer.
# number_2 = int(two_digit_number[1])
# result = number_1 + number_2
# print(result)

#Number Calculation Ordering

# PEMDAS LR
# (Parentheses)   = ()
# Exponenets      = **
# Multiplication  = *
# Division        = /
# Addition        = +
# Substraction    = -

#Follows this, left to right in a calculation
# ()
# **
# */
# = -

#Answer here will be 7 the program does (3*3) = 9 then 3 / 3 = 1 then 9 + 1 = 10 then 10 - 3 = 7
# print(3 * 3 + 3 / 3 - 3)

#Remeber Parathensis are worked out first!! This will be 3 by isoalting calculations to get calcs done firts.
# print(3 * (3 + 3) / 3 - 3)

#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#Example Input
# weight = 80 , height = 1.75
# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
#output as whole number

# height = input("Input your Height in m : ")
# weight = input("Input your weight in kg : ")
# float_height = float(height)
# int_weight = int(weight)
# bmi = int_weight / float_height ** 2
# print(int(bmi))

#or

# height = input("Input your Height in m : ")
# weight = input("Input your weight in kg : ")
# bmi = int(weight) / float(height) ** 2
# print(int(bmi))
