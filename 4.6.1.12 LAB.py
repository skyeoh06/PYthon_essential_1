# What happens when you attempt to run the following snippet?
my_tup = (1, 2, 3)
print(my_tup[2])
>> 3

# What is the output of the following snippet?
tup = 1, 2, 3
a, b, c = tup

print(a * b * c)
>> 6

#Complete the code to correctly use the count() method to find the number of duplicates of 2 in the following tuple.
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2) # Write your code here.

print(duplicates) 

# Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    # Write your code here.
    d3.update(item)

print(d3)

# Write a program that will convert the my_list list to a tuple.
my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)# Write your code here.

print(t)

# Write a program that will convert the colors tuple to a dictionary.
colors = (("green", "#008000"), ("blue", "#0000FF"))

# Write your code here.
colors_dictionary = dict(colors)
print(colors_dictionary)

# What will happen when you run the following code?
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)
> {"A": 1, "B": 2}

# What is the output of the following program?
colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)

>> 
white : (255, 255, 255)
grey : (128, 128, 128)
red : (255, 0, 0)
green : (0, 128, 0)

