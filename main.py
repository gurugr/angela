n = int(input("Enter the number : "))

# def prime_checker(number):
#   for num in range(2,number):
#     if number % 2 ==0:
#       print("no prime")
#       break
#   else:
#     print("prime")

def prime_checker(number):
  is_prime = True
  for x in range(2,number):
    # 5 % 2 = 1
    # 5 % 3 = 2
    # 5 % 4 = 1
    if number % x == 0:
      is_prime = False
  if not is_prime:
    print("not prime")
  else:
    print("prime")

prime_checker(number=n)