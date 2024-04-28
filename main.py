# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
month = int(input("Enter a month (numeric): "))
day = int(input("Enter a day: "))
year = int(input("Enter a four-digit year: "))
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

month_day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

#year = None
#month = None
#day = None

# Get the year, then the month, then the day
#housekeeping()

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif day < MIN_DAY or day > month_day[month]:  # invalid day for the given month
    validDate = False


# Test to see if date is valid and output date and whether it is valid or not

#endOfJob()
if validDate == True:
    # Output statement
  print(month,"/",day,"/",year, "is a valid date")
else:
    # Output statement
  print(month,"/",day,"/",year, "is an invalid date")
  