#Topic:
#-----------------------------
# Import the modules
import sys
import random
ans = True
#This generates a random number and prints a different value every time
#exit when value entere
while ans:
    question = input("Enter a number (1-8): (press enter to quit) ")
    answers = random.randint(1,8)
    ans = True
    print
    if (question == "" or question == 'q'):  break
    elif answers == 1:  print("It is certain")
    elif answers == 2:  print("Outlook good")
    elif answers == 3:  print("You may rely on it")
    elif answers == 4:  print("Ask again later")
    elif answers == 5:  print("Concentrate and ask again")
    elif answers == 6:  print("Reply hazy, try again")
    elif answers == 7:  print("My reply is no")
    elif answers == 8:  print("My sources say no")
    
# if (question == "" or question == 'q'):  sys.exit() or break
