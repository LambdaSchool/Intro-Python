# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
# Use the sys module to look for command line arguments in the `argv` list
# variable.
#
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.

# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.

# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.

import sys
import calendar
import datetime


year = input("Enter year: ")
month = input("Enter month: ")
now = datetime.datetime.now()

if not year and not month:
    year = now.year
    month = now.month
elif not year:
    year = now.year
    month = int(month)
elif not month:
    month = now.month
    year = int(year)
else:
    year = int(year)
    month = int(month)
    
def printCal(year, month):
    print(calendar.month(year,month))

printCal(year, month)
