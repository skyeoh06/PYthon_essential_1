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
