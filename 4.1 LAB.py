# 1.4
def message():
    print("Enter a value: ")

print("We start here.")
print("We end here.")
>>
We start here.
We end here.

def message():
    print("Enter a value: ")

print("We start here.")
message()
print("We end here.")

>>
We start here.
Enter a value: 
We end here.

# 1.5
print("We start here.")
message()
print("We end here.")


def message():
    print("Enter a value: ")

>> NameError: name 'message' is not defined

# 1.6

def hi():
    print("hi")

hi(5)
>> TypeError: hi() takes 0 positional arguments but 1 was given
