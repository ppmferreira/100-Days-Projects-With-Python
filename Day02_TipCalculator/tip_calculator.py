print("Hello, Welcome to Tip Calculator")
total_bill = float(input(f"Use Only numbers! What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? "))
percentage = percentage/100
many_people = float(input("How many people are splitting the bill? "))

final_value = ((total_bill + total_bill * percentage)/many_people)

print(f"Each person should pay: ${final_value}")