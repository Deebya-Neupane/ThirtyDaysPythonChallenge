# Example file for timedelta objects.
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Construct a basic timedelta and print it.
print(timedelta(days=365, hours=8, minutes=45))  
# Print today's date.    
now = datetime.now()
print("Today is: " + str(now))
# Print today's date one year from now.
print("One year from now, it will be: " + str(now + timedelta(days=365)))
# Create a timedelta that uses more than one argument.
print("In 2 days and 2 weeks, it will be: " + str(now + timedelta(days=2, weeks=2)))

# Calculate the date 2 weeks ago, formatted as a string.
t = datetime.now() - timedelta(weeks=2)
s = t.strftime("%A %B %d, %Y")
print("Two weeks ago it was: " +s)

# How many days until my birthday?
today = date.today()
mbd = date(today.year, 1, 14)
# Use date comparison to see if your birthday has already gone for this year.
# if it has, use the replace() function to get the date for next year.
if mbd < today:
   print("My birthday already went by %d days ago." % ((today-mbd).days))  
   mbd = mbd.replace(year = today.year+1)
# Now calculate the amount of time until my birthday.
time_to_mbd = mbd - today
print("It's just ", time_to_mbd.days, "days until my birthday.")   
  