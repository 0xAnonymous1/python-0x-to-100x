print("Hello Sir, welcome to the rollercoster!")
hight=float(input("Please enter your hight:"))
if hight>=120:
  print("You can ride Sir!")
  age=int(input("Please enter your age:"))
  if age>=18:
    print('Plz pay $5 💵')
  elif   age>18:
    print("pay $7 💵")
  elif age>12:
    print("pay $12 💵")
  else:
    print("you are not allowed to ride 😒 ") 
else:
    print("Sorry you can't ride")
