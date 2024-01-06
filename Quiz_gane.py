print("Welcome to the quiz game")

questions = [{"ques":"What is a correct syntax to output 'Hello World' in Python?","answer":"D"},
{"ques":"How do you insert 'COMMENTS' in Python code?","answer":"A"}]

answer = [["A: p ('Hello World')","B: print 'Hello World'","C: printf 'Hello World'","D: print ('Hello World')"],
["A: # command","B: // command","C:-- command"]]

for question in range(len(questions)):
      print(questions[question]["ques"])