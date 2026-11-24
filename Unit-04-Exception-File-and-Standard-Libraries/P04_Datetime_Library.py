
from datetime import datetime

# Current date and time
now = datetime.now()

print("Current Date and Time:", now)

# Extract day, month and year
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)

# Calculate difference between two dates
date1 = input("Enter first date (YYYY-MM-DD): ")
date2 = input("Enter second date (YYYY-MM-DD): ")

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

difference = abs((d2 - d1).days)

print("Difference Between Dates:", difference, "days")