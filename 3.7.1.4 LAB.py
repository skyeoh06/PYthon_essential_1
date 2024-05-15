# Multidimensional nature of lists: advanced applications
from random import random 
temps = [[round(random()*40,1) for h in range(24)] for d in range(31)]
total = 0.0

for day in temps:
    total += day[11]

average = round(total / 31,1)

print("Average temperature at noon:", average)

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)
hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

>>
Average temperature at noon: 16.3
The highest temperature was: 40.0
10 days were hot.
