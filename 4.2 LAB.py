# 1.2
def message(number):
    print("Enter a number:", number)

message()
>> TypeError: message() missing 1 required positional argument: 'number'

def message(number):
    print("Enter a number:", number)

message(1)
>> Enter a number: 1

def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)
>>
Enter a number: 1
1234

# 1.3
def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")

>>
Enter telephone number 11
Enter price number 5
Enter number number number

# 1.4
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

>>
Hello, my name is Luke Skywalker
Hello, my name is Jesse Quick
Hello, my name is Clark Kent

$ 1.5
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

>> 
Hello, my name is James Bond
Hello, my name is Luke Skywalker

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(surname="Skywalker", first_name="Luke")
>>
introduction(surname="Skywalker", first_name="Luke")
TypeError: introduction() got an unexpected keyword argument 'surname'

# 1.6
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Call the adding function here.
adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)
adding(3, a = 1, b = 2)
>>
1 + 2 + 3 = 6
2 + 3 + 1 = 6
3 + 2 + 1 = 6
adding(3, a = 1, b = 2)
TypeError: adding() got multiple values for argument 'a'

# 1.7
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Call the function here.
introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")
>>
Hello, my name is James Doe
Hello, my name is Henry Smith
Hello, my name is William Smith

def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction()
introduction(last_name="Hopkins")
>>
Hello, my name is John Smith
Hello, my name is John Hopkins
