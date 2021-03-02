pizza = input("What is the pizza size 'l'for Larg, 'm'for mediam, 's'for small : ")
total = 0
if pizza == "s":
  print("Pizza is $15 ")
  total +=15
  pepperoni = input("Do you want add extra pepperoni? , 'y' for Yes ")
  if pepperoni == "y":
    total += 2
    print("Extra Pepperoni is $2 ")
else:
  if pizza == "l":
    print("Pizza is $25 ")
    total += 25
  else:
    print("pizza is $ 20 ")
    total +=20
  pepperoni = input("Do you want add extra pepperoni? , 'y' for Yes ")
  if pepperoni == "y":
    print("Extra Pepperoni is $3 ")
    total += 3
  
cheese = input("Extra cheese $1, Do you want 'y'")
if cheese == "y":
  total += 1
  print("Extra Cheese is $1 ")
  print(f"Total bill is : ${total}")
else:
  print(f"Total bill is : ${total}")





    




