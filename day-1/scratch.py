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