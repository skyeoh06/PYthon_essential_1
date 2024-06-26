# 1.6
# Objectives
# becoming familiar with the print() function and its formatting capabilities;
# experimenting with Python code.
# Scenario
# The print() command, which is one of the easiest directives in Python, simply prints out a line to the screen.

# In your first lab:

# use the print() function to print the line Hello, Python! to the screen. Use double quotes around the string;
print("Hello, Python!")
>> Hello, Python!
# having done that, use the print() function again, but this time print your first name;
print("Hello, Yeoh!")
>> Hello, Yeoh!
# remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?
print(Hello, Python!)
>> SyntaxError: invalid syntax
# then, remove the parentheses, put back the double quotes, and run your code again. What kind of error is thrown this time?
print "Hello, Python!"
>> SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello, Python!")?
# experiment as much as you can. Change double quotes to single quotes, use multiple print() functions on the same line, and then on different lines. See what happens.
print('Hello, Python!')
>> Hello, Python!
print('Hello, Python!')print('Hello, Python!')
>> SyntaxError: invalid syntax
print('Hello, Python!')
print('Hello, Yeoh!')
>> Hello, Python!
   Hello, Yeoh!

# 1.8
print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")
>> The itsy bitsy spider climbed up the waterspout.
   Down came the rain and washed the spider out.

# 1.9
# added one empty print() function invocation
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")
>>
The itsy bitsy spider climbed up the waterspout.

Down came the rain and washed the spider out.


# 1.10
# Both the backslash and the n form a special symbol named a newline character, which urges the console to start a new output line.
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")
>>
The itsy bitsy spider
climbed up the waterspout.

Down came the rain
and washed the spider out.

# 1.11
print("\")
>> SyntaxError: EOL while scanning string literal
print("\\")
>> \

# 1.12
# using multiple arguments
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
>> The itsy bitsy spider climbed up the waterspout.

# 1.13
# The positional way of passing the arguments
print("My name is", "Python.")
print("Monty Python.")
>> 
My name is Python.
Monty Python.

# 1.14
# the keyword arguments
# the end keyword argument determines the characters the print() function sends to the output once it reaches the end of its positional arguments.
print("My name is", "Python.", end=" ")
print("Monty Python.")
>> My name is Python. Monty Python.

# 1.15
# the keyword arguments
print("My name is ", end="")
print("Monty Python.")
>> My name is Monty Python.

# 1.16
# The keyword argument that can do this is named sep (like separator).
print("My", "name", "is", "Monty", "Python.", sep="-")
>> My-name-is-Monty-Python.

# 1.17
# Both keyword arguments may be mixed in one invocation
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
>> My_name_is*Monty*Python.*

# 1.18
# Objectives
# becoming familiar with the print() function and its formatting capabilities;
# experimenting with Python code.
# Scenario
# Modify the first line of code in the editor, using the sep and end keywords, to match the expected output. Use the two print() functions in the editor.

# Don't change anything in the second print() invocation.

# Expected output
# Programming***Essentials***in...Python

print("Programming","Essentials","in",end="...",sep="***")
print("Python")


