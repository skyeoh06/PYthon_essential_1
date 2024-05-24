# 1.4
# The exception proves the rule
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')
>>
Enter a natural number: 8
The reciprocal of 8 is 0.125
Enter a natural number: j
I do not know what to do.

# 1.5
# How to deal with more than one exception

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 
>>
Enter a natural number: 9
The reciprocal of 9 is 0.1111111111111111
Enter a natural number: 0
Division by zero is not allowed in our Universe.
Enter a natural number: n
I do not know what to do.
Enter a natural number: @
I do not know what to do.

# 1.6
# The default exception and how to use it
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
>>
 Enter a natural number: 1]
I do not know what to do.
Enter a natural number: .............
I do not know what to do.
Enter a natural number: g0
I do not know what to do.

while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")

>>
Enter an integer number: 89
44.5
Enter an integer number: jk
Warning: the value entered is not a valid number. Try again...
Enter an integer number: 16
8.0

while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")
>>
Enter an int number: 0
Wrong value or No division by zero rule broken.
Enter an int number: l
Wrong value or No division by zero rule broken.
Enter an int number: 9
0.5555555555555556

