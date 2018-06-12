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
day=12
month=6
name=raw_input("what is your name?")
#firstletter=name[0].upper()
#name=name[1:].lower()
#grade=int(raw_input("what is your grade?"))
#print str(firstletter+name) + ", you will graduate from high school in " + str(13-grade) + " years."
birth_month=int(raw_input("enter your birth month as a number"))
birth_day=int(raw_input("what is the day of the month you were born?"))
age=int(raw_input("how old are you?"))
if birth_month >=month:
   m=birth_month-month
else:
   m=12-(month-birth_month)
if birth_day >=day:
    d=birth_day-day
else:
   m=m-1
   d=31-day+birth_day
print str(name) + ", you have " + str(m) + " months and " + str(d) + " days till your birth day."
if age>=13 and age>=17:
   print "you can see g, pg, pg-13, and R."
elif age>=13:
   print "you can see g, pg, and pg-13."
else:
   print "you can see g, and pg."