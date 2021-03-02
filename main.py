height = float(input("Enter your Height :"))
bill = 0

if height > 120:
  age = int(input("Enter your Age: " ))

  if age <= 12:
    print("ticket is $5")
    bill +=5
  elif age >12 and age <=18:
    print("ticket is $7")
    bill +=7
  else:
    print("ticker is $12")
    bill +=12

  photo = input("You want a photo? ")
  if photo == "y" or photo == "Y":
    bill +=3
  print(f"Total bill is ${bill}")

else:
  print("Sorry, Your are not eligible for the rollercost.")


    




