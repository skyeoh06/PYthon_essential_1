# 1.15
# Binary left shift and binary right shift
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
>>
17 68 8

# 1.6
# Summary
# & does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
# | does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
# ˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
# ^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
# >> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
# << does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))
>> False

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
>> 0 5 -5 1 1 16
