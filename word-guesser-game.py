import random 

#choice the word randomly
heart = ["❤️","❤️","❤️","❤️","❤️","❤️"]
words = ["Apple", "Orange","Mango", "Onion"]
chosen_word = random.choice(words)
print (chosen_word)

# give the hint for the player
x = words.index(chosen_word)
print (x)
hint = ["I am a fruit, red in color","I am a fruit, I have 11 brothers",
         "I am a fruit, yellow in color","I will make you to cry when you kill me, and i make food delicious"]

print("hint is ",hint[x])

#start the game 

for i in range(len(chosen_word)):
      print("'_'",end='')

# get input from user
choice = list(chosen_word)

while True:
      print("\n your have",heart)
      player_choice = input("enter the letter: ")
      if player_choice in choice:
            print("you are correct, way to go")
      if player_choice not in choice:
            print("oops! you are wrong")
            heart.pop()
            
            

