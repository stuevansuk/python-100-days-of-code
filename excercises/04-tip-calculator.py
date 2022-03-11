#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# Each person should pay: $19.93

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? : "))
tip_amount = int((input("How much tip would you like to give? : ")))
bill_with_tip = tip_amount / 100 * total_bill + total_bill
people_split = int(input("How many people to split the bill? : "))
final_amount = bill_with_tip / people_split
final_amount = "{:.2f}".format(final_amount) #String Formating, https://thepythonguru.com/python-string-formatting/ - 
print(f"Each Person Should Pay: £ {final_amount}")

