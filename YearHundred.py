################################################
#  Enter the name and age of a user and tell them
#  When they are going to be 100 years old
################################################

from datetime import datetime
name = raw_input("What's your name girl: ")
age = input("Its ebarassing to ask but whats you age: ")
year = str((datetime.today().year-age)+100)
print("Hey " + name + " you will be 100 years old in the year " + year)


#################################################
#

