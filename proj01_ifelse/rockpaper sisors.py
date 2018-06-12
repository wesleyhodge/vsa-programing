loop_control=0
while loop_control=0
    p1=raw_input("player 1 enter rock, paper, or scissors")
    p2=raw_input("player 2 enter rock, paper, or scissors")
    if p1=="rock" and p2=="scissors":
        print "player 1 won."
    elif p1=="scissor" and p2=="rock":
        print "player 2 won."
    elif p1=="rock" and p2=="rock":
        print "tie"
    elif p1=="scissors" and p2=="scissors":
        print "tie"
    elif p1=="paper" and p2=="rock":
        print "player 1 won"
    elif p1=="rock" and p2=="paper":
        print "player 2 won"
    elif p1=="paper" and p2=="paper":
        print "tie"
    elif p1=="scissors" and p2=="paper":
        print "player one won"
    elif p1=="paper" and p2=="scissors":
        print "player 2 won"
    else:
        print "incorrect spelling"