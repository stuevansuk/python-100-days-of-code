#Data Types

#String Data Type, Print Character of String using [] Subscripting
print("Hello"[4])
print("123") 

#Integer - Use _ to make number eeasier readable in code, program will drop them
print(123 + 345)
print(123_456_789)

#Float number with decimal point 3.142

#Boolean, are either True or Fale

#Converting Data Types
num_char = len(input("what is you name? : "))
str_num_char = str(num_char)
print("Your name has " + str_num_char + " characters!")

#Prints Type will be a float
a = 123
print(type(a))

#Prints Type, will be a string
a = str(123)
print(type(a))

#Prints type, will be a float
a = float(123)
print(type(a))

# Will print the addition of 70 + 100.5 becuase these are int and flots
print (70 +float(100.5))

#Will print 70100 as this is defining numbers as a string
print (str(79) + str(100))

#Challenge 
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#Example input = 39 Exmple output 3 + 9 = 12

num_1 = int(input("Number 1 : "))
num_2 = int(input("Number 2 : "))
print(num_1 + num_2)

two_digit_number = input("Provide a 2 Digit Number : ")
number_1 = int(two_digit_number[0]) # Gets 1st Character of the String and sets it as an integer.
number_2 = int(two_digit_number[1])
result = number_1 + number_2
print(result)

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
print(3 * 3 + 3 / 3 - 3)

#Remeber Parathensis are worked out first!! This will be 3 by isoalting calculations to get calcs done firts.
print(3 * (3 + 3) / 3 - 3)

#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#Example Input
# weight = 80 , height = 1.75
# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
#output as whole number

height = input("Input your Height in m : ")
weight = input("Input your weight in kg : ")
float_height = float(height)
int_weight = int(weight)
bmi = int_weight / float_height ** 2
print(int(bmi))

#or

height = input("Input your Height in m : ")
weight = input("Input your weight in kg : ")
bmi = int(weight) / float(height) ** 2
print(int(bmi))

#Rounding Numbers and floating points
print(8/3)
print(round(8/3))
print(round(8/3,2))

#Floor Division, this gives you a flat integer, but removes the float so not useful.
print(8//3) 
print(4//2)

#Allows you to do short hand do to ongoing maths
result = 4/2
result /=2 
print(result)

#Maniupaltes valute based on previous value using + / - operators
score = 0
print(score)
score +=1
print(score)

#Using FString, encorporate different value types without using str(), int() etc all over the place
score = 0 #integer
height = 1.8 #float
isWinning = True #boolean
print(f"Your score is {score}, your height is {height}, are you winning {isWinning}")

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.

days_year = 365
weeks_year = 52
months_year = 12 

age = input("What is your current age : ")
age_as_int = int(age)
death = 90
years_left = death - age_as_int
days_left = int(years_left) * days_year
weeks_left = int(years_left) * weeks_year
months_left = int(years_left) * months_year
message = f"You have {days_left} days {weeks_left} weeks {months_left} months left"
print(message)