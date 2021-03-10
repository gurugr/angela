from replit import clear
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ',',', '.', '=','-', '@', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0','+']
print(len(alphabet))

def caeser(plan_text,shift_amount,ciper_direction):

  cipher_letter = ""
  new_index = None
  for char in plan_text:
    if char in alphabet:
      index = alphabet.index(char)
      new_index = (index + shift_amount)
      if ciper_direction == "decode":
        new_index = (index - shift_amount)
      new_index = new_index % len(alphabet)
      cipher_letter += alphabet[new_index]
    else:
      cipher_letter += char

  print(f"The {ciper_direction}d text is {cipher_letter}")

while True:
  continue_game = input("Do you wan to continue the game 'yes' or 'no' ?\n")
  if continue_game == "yes".lower():
    clear()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    
    caeser(plan_text=text,shift_amount=shift,ciper_direction=direction)
       
  else:
    print("Good Bye")
  
  
  

# encode = True
# while encode:
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")

#   text = input("Type your message: \n").lower()
#   shift = int(input("Type the shift number: \n"))
  
#   shift_list = []
#   def encrypt(plan_text,shift_amount,direction):
  
#     new_shift_list = []
#     new_plan_text = ""
#     if direction == "encode":
#       for x in plan_text:
#         index = alphabet.index(x)
#         new_index = index + shift_amount
#         if new_index > len(alphabet):
#           var = new_index - len(alphabet)
#           new_shift_list.append(var) 
#         else:
#           new_shift_list.append(new_index) 
      
#       for index in new_shift_list:
#         new_plan_text += alphabet[index]
#     elif direction == "decode":
#       for text in plan_text:
#         index = alphabet.index(text)
#         new_index = index - shift_amount
#         print(new_index, end=" ")
#         new_plan_text += alphabet[new_index]
#         encode = False
    

#     print("New shift amount :",new_shift_list)
#     print("plan text :",plan_text)
#     print("New plane text :", new_plan_text)


#   encrypt(text,shift,direction)

