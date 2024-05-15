# 1.1
2 == 2
>> True
2 == 2.
>> True
1 == 2
>> False

# 1.2
# Equality: the equal to operator (==)
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)
>>
True
False

# Inequality: the not equal to operator (!=)
var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)
>>
False
True

# 1.4
# Scenario
# Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.

# Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.

# Test Data

# Sample input: 55

# Expected output: False

# Sample input: 99

# Expected output: False

# Sample input: 100

# Expected output: True

# Sample input: 101

# Expected output: True

# Sample input: -5

# Expected output: False

# Sample input: +123

# Expected output: True

n = int(input("Please input a number: "))
print(n>=100)
>>
Please input a number: 55
False
Please input a number: 99
False
Please input a number: 100
True
Please input a number: 101
True
Please input a number: -5
False
Please input a number: +123
True
