# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in a:
    if item < 5:
        print item
print "done"
#and write a program that prints out all the elements of the list that are less than 5.






#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for place in c:
    for spot in b:
        if spot== place in c:
            print spot
            break
print "done"
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.





#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
for area in d:
    if area == "a":
        area="*"
    print area
print "done"
# and write a program that replaces all “a” with “*”.









#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.
e=[]
ui=raw_input("enter a word")
for letter in ui:
    e.append(letter)
print e







