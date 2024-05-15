# 1.2
# Lists
numbers = [10, 5, 7, 2, 1]
print("List content:", numbers)  # Printing original list content.
>> List content: [10, 5, 7, 2, 1]

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers)  # Printing current list content.

>>
Original list content: [10, 5, 7, 2, 1]

Previous list content: [111, 5, 7, 2, 1]
New list content: [111, 1, 7, 2, 1]

# 1.3
# Accessing list content
# The len() function
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList length:", len(numbers))  # Printing the list's length.
>>
Original list content: [10, 5, 7, 2, 1]

Previous list content: [111, 5, 7, 2, 1]
Previous list content: [111, 1, 7, 2, 1]

List length: 5

# 1.4
# Removing elements from a list
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###

>>
Original list content: [10, 5, 7, 2, 1]

Previous list content: [111, 5, 7, 2, 1]
Previous list content: [111, 1, 7, 2, 1]

List's length: 5
New list's length: 4

New list content: [111, 7, 2, 1]

# 1.5
# Negative indices are legal
numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])
>>
1
2

# 1.8
# Adding elements to a list: append() and insert()
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
>>
4
[111, 7, 2, 1]
5
[111, 7, 2, 1, 4]
6
[222, 111, 7, 2, 1, 4]

# 1.9
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)
>> [1, 2, 3, 4, 5]

# 1.10
# Making use of lis
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
>> 27

# 1.11
# Lists in action
variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2
print("condition 1: ",variable_1,variable_2)

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
print("condition 2: ",variable_1,variable_2)

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
print("condition 3: ",variable_1,variable_2)
>>
condition 1:  1 1
condition 2:  2 1
condition 3:  2 1


