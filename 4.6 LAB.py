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

# 1.5
# How to use a dictionary?
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Print the values here.
print(dictionary['cat'])
>> chat
print(phone_numbers['Suzy'])
>> 22657854310
print(phone_numbers['president'])
>> KeyError: 'president'

words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
>>
cat -> chat
lion is not in dictionary
horse -> cheval

# 1.6
# the keys()
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
>>
cat -> chat
dog -> chien
horse -> cheval

# The sorted() function
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])
>>
cat -> chat
dog -> chien
horse -> cheval

# 1.7
# The items() and values() methods
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)
>>
cat -> chat
dog -> chien
horse -> cheval

for french in dictionary.values():
    print(french)
>>
chat
chien
cheval

# 1.8
# modifying and adding values
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)
>> {'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}

# Adding a new key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)
>> {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}

# update() method
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)
>> {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'duck': 'canard'}

# Removing a key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)
>> {'cat': 'chat', 'horse': 'cheval'}

# popitem() method:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary) 
>> {'cat': 'chat', 'dog': 'chien'}
