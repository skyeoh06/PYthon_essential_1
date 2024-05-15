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


