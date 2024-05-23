# 1.1
# Scopes in Python
def scope_test():
    x = 123


scope_test()
print(x)
>> NameError: name 'x' is not defined

# 1.2
3 A variable existing outside a function has a scope inside the functions' bodies, excluding those of them which define a variable of the same name.
def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
>>
Do I know that variable? 1
1

def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
>>
Do I know that variable? 2
1

# 1.3
# Functions and scopes: the global keyword
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
>>
Do I know that variable? 2
2

# 1.4
# How the function interacts with its arguments
def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)
>>
I got 1
I have 2
1

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
>>
Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [0, 1]
Print #4: [2, 3]
Print #5: [2, 3]

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
>>
Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [3]
Print #4: [3]
Print #5: [3]

# 1.5
var = 2


def mult_by_var(x):
    return x * var


print(mult_by_var(7))    # outputs: 14

def mult(x):
    var = 5
    return x * var


print(mult(7))    # outputs: 35

def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))    # outputs: 49

var = 2
print(var)    # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())    # outputs: 5
print(var)    # outputs: 5

def message():
    alt = 1
    print("Hello, World!")


print(alt)
>> NameError: name 'alt' is not defined

a = 1


def fun():
    a = 2
    print(a)


fun()
print(a)
>> 
2
1

a = 1


def fun():
    global a
    a = 2
    print(a)


fun()
a = 3
print(a)
>>
2
3

a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
fun()
print(a)
>>
2
2
