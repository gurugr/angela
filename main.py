bill = float(input("Enter total bill: " ))
tip = int(input("What percentage tip would you like to give? 10,12 or 15? "))
persons = int(input("How many people to split the bill? "))
tip1 = bill *tip /100
total_with_tip = bill+tip1
person = total_with_tip/persons
final_bill = round(person,2)
final_bill = "{:.2f}".format(person)
print("Each person should pay : $",final_bill)



