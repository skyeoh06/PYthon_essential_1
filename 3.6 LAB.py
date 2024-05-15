# 1.1
# The inner life of lists
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
>> [2]

# 1.2
# Powerful slices
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
>> 
[1]
[8, 6]

# 1.3
# Slices - negative indices
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
>>
[8, 6, 4]
[]

# 1.4
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
>>
[10, 8, 6]
[4, 2]

# 1.5
# slices:del
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)

>>
[10, 8, 6, 4, 2]
[10, 4, 2]
[]
    print(my_list)
NameError: name 'my_list' is not defined

# 1.6
# The in and not in operators
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
>>
False
True
True

# 1.7
# Lists - some simple programs
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
>> 17

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)
>> 17

# 1.8
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")


>> Element found at index 4

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)
>> 4
