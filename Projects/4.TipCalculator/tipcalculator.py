print("Welcome to the tip calculator")
bill=float(input("Enter your bill💵 $"))
tip_percentage=float(input("what percentage tip would you like to give? 10, 20, or other $"))
percentage=((bill/100)*tip_percentage)
total_bill=bill+percentage
print(f"your total bill with tip is: {total_bill}")
no_of_person=int(input("How many people to split the bill:"))
split_bill=round(total_bill/no_of_person,2)
print(f"Each person should pay: {split_bill}")
