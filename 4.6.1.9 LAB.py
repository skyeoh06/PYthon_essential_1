# Tuples and dictionaries can work together
school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# line 2: create an empty dictionary for the input data; the student's name is used as a key, while all the associated scores are stored in a tuple (the tuple may be a dictionary value - that's not a problem at all)
# line 4: enter an "infinite" loop (don't worry, it'll break at the right moment)
# line 5: read the student's name here;
# line 6-7: if the name is an empty string (), leave the loop;
# line 9: ask for one of the student's scores (an integer from the range 0-10)
# line 10-11: if the score entered is not within the range from 0 to 10, leave the loop;
# line 13-14: if the student's name is already in the dictionary, lengthen the associated tuple with the new score (note the += operator)
# line 15-16: if this is a new student (unknown to the dictionary), create a new entry - its value is a one-element tuple containing the entered score;
# line 18: iterate through the sorted students' names;
# line 19-20: initialize the data needed to evaluate the average (sum and counter)
# line 21-23: we iterate through the tuple, taking all the subsequent scores and updating the sum, together with the counter;
# line 24: evaluate and print the student's name and average score.

# Output
Enter the student's name: Bob
Enter the student's score (0-10): 7
Enter the student's name: Andy
Enter the student's score (0-10): 3
Enter the student's name: Bob
Enter the student's score (0-10): 2
Enter the student's name: Andy
Enter the student's score (0-10): 10
Enter the student's name: Andy
Enter the student's score (0-10): 3
Enter the student's name: Bob
Enter the student's score (0-10): 9
Enter the student's name:
Andy : 5.333333333333333
Bob : 6.0
