# marks = input("Enter all the Marks of the students :\n").split(" ")
# for mark in range(0,len(marks)):
#   marks[mark] = int(marks[mark])

# print("Students marks ",marks)

# highest_score = 0
# for mark in marks:
#   if mark > highest_score:
#     highest_score = mark

# print(highest_score)
import random

a =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


b = ['1','2','3','4','5','6','7','8','9','0']

c = ['!','@','#','$','%','^','&','*','(',')']

letters = int(input("How many letters do you want to add :\n"))
numbers = int(input("How many numbers do you want to add :\n"))
symbols = int(input("How many symbols do you want to add :\n"))

password_caractors = (letters+numbers+symbols)

password = []

for x in range(1,letters+1):
  password.append(random.choice(a))

for x in range(1,numbers+1):
  password.append(random.choice(b))

for x in range(1,symbols + 1):
  password.append(random.choice(c))

# Random Password generator

random.shuffle(password)
for x in password:
  print(x,end="")


# total_digits = (letters + numbers + symbols)

# password = []
# for x in random.sample(a,letters):
#   password.append(x)
# for x in random.sample(b,numbers):
#   password.append(x)
# for x in random.sample(c,symbols):
#   password.append(x)

# for p in random.sample(password,total_digits):
#   print(p,end="")















  






