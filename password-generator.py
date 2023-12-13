import string 
import random 

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation 

all_char = letters + numbers + symbols 

for i in range (0,13):
      print(random.choice(all_char),end='')