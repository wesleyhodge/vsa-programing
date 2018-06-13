# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
answer = random.randint(1,9)
loop=4
d=4
while loop != 0:
    guess=raw_input("guess a number")
    if guess=="exit":
        loop=0
    elif int(guess)==answer:
        loop=0
        print "you guessed the number"
    elif int(guess)>answer:
        d=d-1
        loop=loop-1
        print "too high"
    elif int(guess)<answer:
        loop=loop-1
        d=d-1
        print "too low"
if d == 0:
    print "you ran out of gueses"


