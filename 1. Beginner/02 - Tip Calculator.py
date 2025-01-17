#I created a simple calculator to calculate the price of food in a restaurant with techniques learned in the classroom.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
percentage = tip/100 + 1
result = (bill / people) * percentage
print(f"each person must pay: " + str(round(result,2)))
