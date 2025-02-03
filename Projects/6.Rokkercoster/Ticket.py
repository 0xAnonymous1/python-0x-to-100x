bill=0

print("Hello Sir, welcome to the rollercoster!")
hight=float(input("Please enter your hight:"))
if hight>=120:
  print("You can ride Sir!")
  age=int(input("Please enter your age:"))
 
  if age>=18: 
    bill=5
    print('Plz pay $5 💵')
  elif   age>18:
    bill=7
    print("pay $7 💵")
  elif age>12:
    bill=12
    print("pay $12 💵")
  else:
    print("you are not allowed to ride 😒 ")
  
  wants_photo=input("do you want photo? y or N :")
  if wants_photo == "y":
    print(f"your bill is:{bill+3}$")
else:
    print("Sorry you can't ride")
