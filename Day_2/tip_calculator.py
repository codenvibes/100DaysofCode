#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_percentage_float = (tip_percentage/100) + 1 

people = int(input("How many people to split the bills? "))

bill_per_person = round((bill / people) * tip_percentage_float, 2)
final_amount = "{:.2f}".format(bill_per_person)
message = f"Each person should pay ${final_amount}"

print(message)
