# List of priorities
# parentheses()> ** > unary (+/-) > *, /, //, % > +,-
print(2 * 3 % 5)
>>
1

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
>>
10.0

print((2 ** 4), (2 * 4.), (2 * 4))
>> 16 8.0 8

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
>> -0.5 0.5 0 -1

print((2 % -4), (2 % 4), (2 ** 3 ** 2))
>> -2 2 512