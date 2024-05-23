# 1.2
# How to use a tuple?
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

>>
1
1000
(10, 100, 1000)
(1, 10)
1
10
100
1000

my_tuple.append(10000)
del my_tuple[0]
my_tuple[1] = -10
>> AttributeError: 'tuple' object has no attribute 'append'

# 1.3
# the len() function accepts tuples, and returns the number of elements contained inside;
# the + operator can join tuples together (we've shown you this already)
# the * operator can multiply tuples, just like lists;
# the in and not in operators work in the same way as in lists.
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
>> 9
print(t1)
>> (1, 10, 100, 1000, 10000)
print(t2)
>> (1, 10, 100, 1, 10, 100, 1, 10, 100)
print(10 in my_tuple)
>> True
print(-10 not in my_tuple)
>> True

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)
>> (2,) (3, 123) (1,)
