import string 
import random 

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation 

all_char =[]

for i in range (0,5):
      char = random.choice(letters)
      all_char +=char
for i in range (0,4):
      num = random.choice(numbers)
      all_char += num
for i in range (0,3):
      sym = random.choice(symbols)
      all_char += sym
print (all_char)
for i in range(0,10):
      print(random.choice(all_char),end='')