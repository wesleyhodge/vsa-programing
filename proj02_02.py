# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
x = int(raw_input("how many numbers in the fibonacci sequence would you like to see?"))
p = 0
n = 1
c = 0
for w in range(0,x):
    print n
    p = n
    n=c+p
    c=p
y=int(raw_input("how many numbers doubled?"))
p=1
n=2
for r in range(0,y):
    print n
    p=n
    n=p+n
p=0
n=1
c=0
y = int(raw_input("how many numbers in the fibonacci sequence would you like to see?"))
a=0
while a <y:
    print n
    p=n
    n=c+p
    c=p
    a=a+1
