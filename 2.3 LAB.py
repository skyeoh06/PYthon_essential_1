# 1.1 
# Operators - data manipulation tools
print(2+2)
print(2-2)
print(2*2)
print(2/2)
>>
4
0
4
1.0

# 1.2
# Arithmetic operators: exponentiation
# A ** (double asterisk) sign is an exponentiation (power) operator. Its left argument is the base, its right, the exponent.
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
>>
8
8.0
8.0
8.0

# 1.3
# Arithmetic operators: multiplication
# An * (asterisk) sign is a multiplication operator.
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
>> 
6
6.0
6.0
6.0

# Arithmetic operators: division
# A / (slash) sign is a divisional operator.

# The value in front of the slash is a dividend, the value behind the slash, a divisor.
# The result produced by the division operator is always a float,
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
>>
2.0
2.0
2.0
2.0

# 1.4
# Arithmetic operators: integer division
# A // (double slash) sign is an integer divisional operator. 
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
>>
2
2.0
2.0
2.0

print(6 // 4)
print(6. // 4)
>>
1
1.0

# 1.5
# Operators: remainder (modulo)
# The result of the operator is a remainder left after the integer division.
print(14 % 4)
>>
2
# the result is two. This is why:

# 14 // 4 gives 3 → this is the integer quotient;
# 3 * 4 gives 12 → as a result of quotient and divisor multiplication;
# 14 - 12 gives 2 → this is the remainder.

print(12 % 4.5)
>>
3.0

# 1.6
# Operators: addition
print(-4 + 4)
print(-4. + 8)
>>
0
4.0

# The subtraction operator, unary and binary operators
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(+2)
>>
-8
-4.0
-1.1
2

# 1.8
# Operators and their bindings: exponentiation
print(2 ** 2 ** 3)
>>
256

# 2 ** 3 → 8; 2 ** 8 → 256
# the exponentiation operator uses right-sided binding.

