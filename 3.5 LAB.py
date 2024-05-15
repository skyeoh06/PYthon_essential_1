# Sorting a list
my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.
print(my_list)[
>> 8, 6, 2, 4, 10]

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
>> [2, 4, 6, 8, 10]

# The bubble sort - interactive version
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
>>
How many elements do you want to sort: 5
Enter a list element: 55
Enter a list element: 23
Enter a list element: 1
Enter a list element: 89
Enter a list element: 23

Sorted:
[1.0, 23.0, 23.0, 55.0, 89.0]

# summary
a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)
>> [1, 2, 3]

a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)
>> [' ', 'C', 'B', 'A']
