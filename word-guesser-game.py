import random 

#choice the word randomly

heart = ["❤️","❤️","❤️","❤️","❤️","❤️"]
words = ["apple", "orange","mango", "onion"]
chosen_word = random.choice(words)

# give to the hint for the player


value = {"apple":"I am a fruit, red in color",
        "orange":"I am a fruit, I have 11 brothers and sisters",
        "mango":"I am a fruit, yellow in color",
        "onoin":"I will make you to cry when you kill me, and i make food delicious"}
print("\n")
print( f"The hint is  {value[chosen_word]}")

# get input from user

choice = list(chosen_word)
word = []

while (len(choice) != 0 and len(heart) != 0):
      print("\n")
      for i in range(len(choice)):
            print("'_'",end='')
            break
      print("\n your have",heart)
      player_choice = str(input("enter the letter: "))
      if player_choice not in choice:
            print("oops! you are wrong")
            heart.pop()
      if player_choice in choice:
            print("you are correct, way to go")
            choice.remove(player_choice)
            word.append(player_choice) 
      print(word,end='')

      if (len(choice) == 0):
            print("\n you won")
      if (len(heart) == 0):
            print("\n you loose")
            
      
print("\n The chosen word is ", chosen_word)








            
            

