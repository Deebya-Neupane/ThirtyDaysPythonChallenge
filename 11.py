# Example file for working with calendars.

# Import the calendar module.
import calendar

# Create a plain text calendar.
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2022, 1, 0, 0)
print(st)

# Create an HTML formatted calendar.
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2022, 1)
print(st)

# Loop over the days of a month.
# Zeroes mean that the day of the week is in an overlapping month.
for i in c.itermonthdays(2022, 1):
    print(i)

# The calendar module provides useful utilities for the given locale.
# Such as the names of days and months in both full and abbreviated forms.
for name in calendar.month_name:
    print(name)
for day in calendar.day_name:
    print(day)     

# Calculate days based on a rule:consider a family gathering in the first Friday of every month.
# To figure out what days that would be for each month, we can use this script.
print("Family gathering will be on: ")
for m in range(1,13):
    cal =calendar.monthcalendar(2022, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY]!=0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]  
         
    print("%10s %2d" % (calendar.month_name[m], meetday))         