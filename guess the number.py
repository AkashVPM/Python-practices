import random

# rule
print("""Guidelines
You can select the level of hardness as you want.
The number are be in the range of 0 to 50.""")

# level selection 

def level (player_wish):
      if player_wish == "hard":
            life = 5
      elif player_wish == "easy":
            life = 10 

      return life


# select random number

numbers = []
for i in range (1,51):
      numbers.append(i)

hidden_number = random.choice(numbers)



# number closeness checker

def difference (number):

      if number > hidden_number:
            variation = number - hidden_number
            if variation <= 5:
                  print("You are too close")
            elif variation <= 10:
                  print("You are close")
            elif variation <= 20:
                  print("THe value is high")
            elif variation > 20:
                  print("The value is too high")

      if number < hidden_number:
            variation = hidden_number - number
            if variation <= 5:
                  print("You are too close")
            elif variation <= 10:
                  print("You are close")
            elif variation <= 20:
                  print("The value is small")
            elif variation > 20:
                  print("The value is too small")



# guess the number in loop

life = str(input("\nChoice the level of the game play 'Hard' or 'Easy'")).lower()
value = level(life)
base = 0


while (base < value ):

      print(f"\nYou have {value} life")
      
      guesses = int(input("\nEnter the number you gussed: "))
      if guesses == hidden_number:
            print ("\nYou win")
            break
      if guesses != hidden_number:
            difference(guesses)
      value -= 1
      if base == value :
            print("\nYou loose")

print (f"The hiden number is {hidden_number}")
      
            
      


