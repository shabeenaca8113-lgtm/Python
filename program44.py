import time
import datetime
now=datetime.datetime.now()
print("Enter any key to display current date and time:")
input()
print("current date and time:",now)
print("current year:",now.year)
print("Month of the year:",now.month)
print("week number of the year:",now.isocalendar()[1])
print("weekday of the week:",now.strftime("%A"))
print("Day of year:",now.strftime("%j"))
print("Day of month:",now.day)
print("Day of week:",now.weekday())
