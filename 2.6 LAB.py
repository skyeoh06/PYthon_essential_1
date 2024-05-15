# 1.3
# The input() function - prohibited operations
# Testing TypeError message.

anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
>> 
something = anything ** 2.0
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

# 1.4
# Type Casting
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
>> 
Enter a number: 8
8.0 to the power of 2 is 64.0

# 1.5
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
>>
Input first leg length: 22
Input second leg length: 17
Hypotenuse length is 27.80287754891569

# 1.6
# String operators
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
>>
May I have your first name, please? Chloe
May I have your last name, please? Rose
Thank you.

Your name is Chloe Rose.

# 1.7
# Replication
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
>>
+----------+
|          |
|          |
|          |
|          |
|          |
+----------+

