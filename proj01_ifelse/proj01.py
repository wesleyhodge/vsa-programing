# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!
day=11
month=6
name=raw_input("what is your name?")
#firstletter=name[0].upper()
#name=name[1:].lower()
#grade=int(raw_input("what is your grade?"))
#print str(firstletter+name) + ", you will graduate from high school in " + str(13-grade) + " years."
birth_month=int(raw_input("enter your birth month as a number"))
birth_day=int(raw_input("what is the day of the month you were born?"))
if birth_month >=month:
   print str(name) + " you have " + str(birth_month-month) + " months till your birth day and"
else: print str(name) + " you have " + str(12-(month-birth_month)) + " months till your birth day and"
if birth_day >=day:
    print str(birth_day-day) + " days till birth day."



