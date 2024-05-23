# 1.3
# Returning a result from a function
def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))
>>
True
None

# 1.4 
# Effects and results: lists and functions
def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s
print(list_sum([5, 4, 3]))
>> 12
print(list_sum(5))
>> TypeError: 'int' object is not iterable

# 1.5
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))
>> [4, 3, 2, 1, 0]

# 1.11
def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None

def wishes():
    return "Happy Birthday!"

w = wishes()

print(w)    # outputs: Happy Birthday!

def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)

hi_everybody(["Adam", "John", "Lucy"])
>>
Hi, Adam
Hi, John
Hi, Lucy

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))
>>[0, 1, 2, 3, 4]

def hi():
    return
    print("Hi!")

hi()
>> None

def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))
>>
True
False
None

def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11))
>> [0, 2, 4, 6, 8, 10]

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo))
>> [1, 4, 9, 16, 25]

