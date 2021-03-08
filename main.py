import random
from hang_man_ascii import hangman,stages
from replit import clear

print(hangman)
word_list = ["book","computer","pencil","school"]
chosen_word = random.choice(word_list)

display = []
for position in range(len(chosen_word)):
  display.append("_")

last_disp = " ".join([str(eli) for eli in display])
print("Random Word is :",last_disp)

lives = 6

end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  clear()
  for letter in range(len(chosen_word)):
    position = chosen_word[letter]
    if position == guess:
      display[letter] = guess
  last_disp = " ".join(str(eli)for eli in display)
  print(last_disp)
  

  if guess not in chosen_word:
    print(stages[lives])
    lives -=1
    if lives == -1:
      print("You Lost ")
      end_of_game = True
  
  if "_" not in display:
    print("You Won!")
    end_of_game = True




# words = ["book","computer","pencil","school"]
# random_word = random.choice(words)
# print("Random Word is :",random_word)
# random_word_length = range(len(random_word))
# display = []
# for text in random_word_length:
#   display.append("_")
# print(display)

# wrong_guess = 0
# guess_again_and_again = False

# while not guess_again_and_again:
#   guess_word = input("Guess: ")
#   for text in random_word_length:
#     position = random_word[text]
#     if position == guess_word:
#       display[text] = guess_word

#   print(display)

#   if not "_" in display:
#     print("You Won !")
#     guess_again_and_again = True

  
#   if guess_word not  in display:
#     wrong_guess += len(guess_word)
#     print("I am Not in :", wrong_guess)


