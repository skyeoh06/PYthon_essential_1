# Objectives
# Familiarize the student with:
# projecting and writing parameterized functions;
# utilizing the return statement;
# building a set of utility functions;
# utilizing the student's own functions.

# Scenario
# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

def is_year_leap(year):
#
# Write your code here.
    if((year % 400 == 0) or (year % 100 != 0) and(year % 4 == 0)): 
        return True;
    else:
        return False;

def days_in_month(year, month):
#
# Write your new code here.
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
#   
    if is_year_leap(year)and month==2:
        return 29
    else:
        return month_days[month-1]
def day_of_year(year, month, day):
#
# Write your new code here.
    if year<1582:
        return none
    if month>12 or month <1:
        return None
    if day<1 or day>days_in_month(year, month):
        return None
    totaldays=day
    month =month-1
    while month >0:
        totaldays +=days_in_month(year, month)
        month -=1
    return totaldays
    
#

print(day_of_year(2000, 2, 29))
