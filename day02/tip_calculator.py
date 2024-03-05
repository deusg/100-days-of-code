# Day 2 Project: Tip Calculator.

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?: $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15?: "))
tip_percentage = float(tip_percentage / 100)
total_tip_amount = total_bill * tip_percentage
total_bill_with_tip = total_bill + total_tip_amount
num_of_people = int(input("How many people to split the bill? "))
total_bill_per_person = float(total_bill_with_tip) / (num_of_people)
print(f"Each person should pay: ${total_bill_per_person:.2f}")
