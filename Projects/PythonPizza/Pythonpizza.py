# This Python code is a simple program for a pizza ordering system. Here's a breakdown of what the
# code does:
small_pizza = 15
medium_pizza = 20
large_pizza = 25
bill=0
print("Welcome to python pizza 😊")
print("Alert: Plz input capital latters👍")
pizza_size = input("what size pizza do you want? S, M, L :")
add_pepperroni= input("do you want pepproni?(Y ,N):")
if pizza_size =="S" and add_pepperroni == "Y":
  bill=small_pizza+2
if pizza_size =="S" and add_pepperroni == "N":
  bill=small_pizza
if pizza_size=="M" and add_pepperroni == "Y":
  bill=medium_pizza+2
if pizza_size=="M" and add_pepperroni == "N":
  bill=medium_pizza
if pizza_size =="L" and add_pepperroni == "Y":
  bill=large_pizza+3
if pizza_size =="L" and add_pepperroni == "N":
  bill=large_pizza
extra_cheese = input("do you want some extra cheese (Y,N):")
if extra_cheese=="Y":
  bill+=1
  print(f"your bill is ${bill}")
if extra_cheese=="N":
  bill
  print(f"your bill is ${bill}")    

  
  

