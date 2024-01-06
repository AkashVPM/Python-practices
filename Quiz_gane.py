print("Welcome to the quiz game")

questions = [{"ques":"What is a correct syntax to output 'Hello World' in Python?","answer":"D"},
{"ques":"How do you insert 'COMMENTS' in Python code?","answer":"A"}]

answer = [["A: p ('Hello World')","B: print 'Hello World'","C: printf 'Hello World'","D: print ('Hello World')"],
["A: # command","B: // command","C: -- command"]]

def check_answer(guess, correct_answer):
      if guess == correct_answer:
            return True
      else:
            return False

score = 0
for question in range(len(questions)):
      print("\n",questions[question]["ques"])
      for i in answer[question]:
            print(i)

      guess = input("Choose the input 'A','B','C','D'").upper()
      is_correct = check_answer(guess, questions[question]["answer"])
      
      if is_correct:
            print("Correct answer")
            score += 1
      else:
            print("Wrong answer")

print(f"\nYour final score is: {score}/{len(questions)}")
