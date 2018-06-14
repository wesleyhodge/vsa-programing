# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
w12=choose_word(wordlist)
word=[]
blank=[]
us=["_"]
abc=string.lowercase
for letter in w12:
    word.append(letter)
q=0
while q<len(word):
    for letter in us:
        blank.append(letter)
    q=q+1
print "welcome to hangman"
print "I am thinking of a word " + str(len(word)) + " characters long"
r=0
lost=0
while r<8:
    print "you have not guessed " + str(abc)
    print "you have " + str(8-r) + " guesses left"
    print blank
    guess=raw_input("guess a letter")
    abc=abc.replace(guess, "")
    d=0
    a=0
    for letter in word:
        if guess==letter:
            blank[d]=guess
            print "that is the correct letter"
        else:
            a=a+1
        d=d+1
    if a==len(word):
        print "that is not in the letter"
        r = r+1
        lost = lost+1
    elif blank == word:
        print "you got it that is the word, you won"
        r = 8
if lost == 8:
    print "you lost, you ran out of guesses it was "
    print w12


