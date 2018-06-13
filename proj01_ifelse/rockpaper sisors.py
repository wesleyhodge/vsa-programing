import random
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
    elif q=="no" or q=="nope" or q=="exit":
        loop_control=1
    else:
        print "incorrect spelling"
        loop_control=1