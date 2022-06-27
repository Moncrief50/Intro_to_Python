# 1 Try the code below and revise it to current time
# Import all packages in the beginning to avoid errors.
import sys

from datetime import datetime
from datetime import timedelta
from pytils import dt

# Define the function
def main():
    dt = datetime.now()
    utc = datetime.utcnow()
    time_string = dt.strftime("%X")
    """https://strftime.org"""

    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) == 6:
            data = date, time, store, item, cost, payment
        print("{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}")

# 2 Add the timedelta to the datetime and subtract 60 second and added 2 year
print(datetime.now() + timedelta(days=1))
print(datetime.now() - timedelta(seconds=60))
print(datetime.now() + timedelta(days=730))

# 3 Create a timedelta object representing 100 days, 10 hours, and 13 minutes.
# timedelta representing -1 microseconds
d = timedelta(microseconds = -1)
print(d.days, d.seconds, d.microseconds)

# timedelta representing 100 days, 10 hours, and 13 minutes
s = timedelta(days=100, seconds=36000, microseconds=780000000)
print(s.days, s.seconds, s.microseconds)

# 4 Write a function that takes two arguments (feet and inches) with this time object
# get current date
# Name the current time
datetime_object = datetime.now()
# Print the type of datetime_object
print('Type :- ', type(datetime_object))

# Creating the feet, time, and date function
def ft_in_time(F,I,D):
    print(F, ": Feet")
    print(I, ": Inches")
    print("Today's Date:", datetime_object)

F = input("Input size in Feet :")
I = input("Input size in Inches :")
D = datetime_object
ft_in_time(F, I, D)




