#This Script when run returns the exact date and time. I don't use exact lightly because
#this script gives you several decimal places off of the seconds. 
#I consulted the datetime documentation to write this script. Linked here: https://docs.python.org/3/library/datetime.html
#To run this code in command line you will have to type "python Project1.py"


import datetime

DateInfo = datetime.datetime.now()

print ("Today's Date and Time: = %s" % DateInfo)
