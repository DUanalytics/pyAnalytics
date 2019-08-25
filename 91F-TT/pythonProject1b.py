#Topic:
#-----------------------------
#Minor Projects
#https://www.pythonforbeginners.com/code/magic-8-ball-written-in-python
#Ex1: Magic and Ball
#The Magic 8-ball is a fortune telling toy created by Mattel in the 1950s.
#https://www.indra.com/8ball/front.html
#https://teachwithict.weebly.com/magic-8-ball1.html
#https://www.youtube.com/watch?v=vZRrg6Nl-1E
#https://www.youtube.com/watch?v=0-FYc-eEDa0
#https://en.wikipedia.org/wiki/Magic_8-Ball
# Import the modules
import random, string
#using 8 possible answers, but please feel free to add more asyou wish. 
#create 20 choices : ans1, ans2, ans3
ans1 =("It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes", "Most likely. ", "Outlook good.", "Yes", "Signs point to yes")
ans2 = ("Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again")
ans3 = ("Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.")
answersA = ans1 + ans2 + ans3
answersA  #tuple
len(answersA)  #20 answers
random.sample(set('abcdefghijklmnopqrstuvwxyz'), 1)  #random character
random.sample(list(answersA),1)  #every time you run, get different value - use this concept

print("Ask the magic 8 ball a question: (press enter to quit) ")
ans1 = True
while ans1:
    q2 = input("Enter a number (1-8): (press enter to quit) ")
    a2 = random.randint(1,8)
    ans1 = True
    print
    if (q2 == "" or q2 == 'q'):  break
    else :  print(answersA[a2])

