import random

stages = ['''
      _______
     |/    |
     |    (_)
     |    \|/
     |     |
     |    / \
     |
 jgs_|___''',
 '''   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 jgs_|___''','''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |

 jgs_|___''','''   
      _______
     |/      |
     |      (_)
     |      \|/
     |
 jgs_|___''','''
       _______
     |/      |
     |      (_)
     |       |
     |
 jgs_|___''','''
      _______
     |/      |
     |      (_)
     |
 jgs_|___''',''' 
      _______
     |/      |
     |      

     |
 jgs_|___''',]

words = ["pencil","book","computer"]

rand_word = random.choice(words).lower()

display = []
len_word = len(rand_word)
for word in range(len_word):
  display.append("_")



print(display)
print(rand_word)
guess_time = 0
success_word_count = 0


counter = False
while not counter:
  guess_word = input("Enter a tetter : \n")
  guess_time +=1
  for letter in range(len_word):
    position = rand_word[letter]
    if position == guess_word:
      display[letter] = position
      success_word_count +=1
  print(display)

  # print("guess_time :",guess_time)
  # print("success_word_count :",success_word_count)
  stages_tracking = (success_word_count - guess_time)
  # print("stages_tracking :",stages_tracking)

  if not stages_tracking == -8:
    current_stages = stages[stages_tracking]
    print(current_stages)
  else:
    print("You Dead ")
    counter = True
  

  if "_" not in display:
    print("You Won!")
    counter = True





# counter = 0
# while counter < len_word:
#   guess_word = input("Enter a tetter : \n")
#   for letter in range(len_word):
#     position = rand_word[letter]
#     if position == guess_word:
#       display[letter] = position
#       counter +=1
#   print(display)


# print("You Won!")










