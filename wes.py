import random
name=raw_input("what is your name?")
name=name.lower()
print "hello " + name + " pleased to meet you."
hayd=raw_input("how are you? (good, bad, ok, awesome, horrible)")
hayd=hayd.lower()
if hayd=="good":
    print "I am glad you are having a good day"
elif hayd=="bad" or hayd=="horrible":
    print "that is not good"
    print "just relax"
elif hayd=="awesome":
    print "that is great"
else:
    print "ok"
read=raw_input("do you like to read?(yes or no)")
if read=="yes":
    print "cool"
elif read=="no":
    print "books are fun try reading one"
why=raw_input("do you like video games(yes or no) ")
if why=="no":
    h=raw_input("have you played on a game boy?(yes, no, or what is a game boy)")
    if h=="yes":
        print "ok"
    elif h=="no":
        print "you should try it out"
    elif h=="what is a game boy":
        print "A game boy is a small devise that has no back light. It is hand held and uses cartrages. It is a cool devise you should look it up "
elif why=="yes":
    print "cool so do I"
c=raw_input("have you heard of city of ember?(yes or no)")
if c=="yes":
    print "I like it"
    d=raw_input("do you?(yes or no)")
    if d=="yes":
        print "me too"
    elif d=="no":
        print "ok"
elif c=="no":
    print "it is a cool book series in the first book the characters live in a under ground city that they have to leave because it is failing"
print "let's play rock, paper, scissors"
loop_control=0
while loop_control==0:
    p1=raw_input("player 1 enter rock, paper, or scissors:")
    p1=p1.lower()
    p2=random.randint(1,3)
    if p1=="rock" and p2==3:
        print "computer played scissors"
        print "player 1 won."
    elif p1=="scissor" and p2==1:
        print "computer played rock"
        print "computer won."
    elif p1=="rock" and p2==1:
        print "computer played rock"
        print "tie"
    elif p1=="scissors" and p2==3:
        print "computer played scissors"
        print "tie"
    elif p1=="paper" and p2==1:
        print "computer played rock"
        print "player 1 won"
    elif p1=="rock" and p2==2:
        print "computer played paper"
        print "computer won"
    elif p1=="paper" and p2==2:
        print "computer played paper"
        print "tie"
    elif p1=="scissors" and p2==2:
        print "computer played paper"
        print "player one won"
    elif p1=="paper" and p2==3:
        print "computer played scissors"
        print "computer won"
    else:
        print "incorrect spelling"
    q=raw_input("would you like to keep playing? (lower case)(yes or no)")
    if q=="yes" or q=="yea" or q=="yeah" or q=="sure" or q=="ok":
        loop_control=0
    elif q=="no":
        print "bye"
        loop_control=1
    else:
        loop_control=1