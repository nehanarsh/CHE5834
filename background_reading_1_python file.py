'''
Updated on Sep. 16, 2023

@author: olgap
'''

''' Welcome to the code-along for the first Background Reading,
BR 1 ! 

As you read through the BR 1 pdf doc (available on D2L), feel
free to test out the bits of this accompanying code, which has already 
been pre-made for you (this file).  

Do whatever you like with this file. This is for you to learn and play. This file 
does not need to be submitted anywhere.

PS. As you go through this, it may be easier to "comment out" the lines of code
you don't want to run at any given moment, to avoid a bunch of cascading print 
statements from the entire file.

Have fun & good luck! - Olga''' 

# imports a built-in function that already lives in your Python download
import random

#this will work because there is no weird spacing before the code starts
print('indentation is important')
# this has a few random spaces before the code starts. Comment out the line
# below to clear the error!
    print('indentation is important')

#this will show the difference between printing one versus multiple strings
print('I love nuclear engineering')
#default spaces between different strings printed
print('I', 'love', 'nuclear', 'engineering')


''' Variables '''

#assigning a string to the variable called x
x = 'Nuclear Engineering is a cooler course than Nuclear Reactor Physics'
print(x)
#printing the character x
print('x')

#prints the first letter in the string
print(x[0])
#prints the last letter in the string
print(x[-1])
#determines the length of the string
y = len(x)
print (y)
#prints the entire string
print(x[0:67])
# prints the entire string
print(x[0::])

''' Data Types '''

#assigning the string 2 to the variable y
y = '2'
print(y)
#converts y from a string to a float
y = float(y)
print(y)

''' Overloading Strings '''

x = 'checking how '
y = 'math operators work'

z = x + y
print(z)

z = x * 3
print (z)

# z = x * 4.1
# print (z)

''' Lists '''

listofstrings = ['A', 'B', 'C']
# determines length of list above (how many comma separated entries)
lengthlist = len(listofstrings)

# print the second element of the list (first item is at index 0, not 1)
print(listofstrings[1])
# print the last element of the list
# note: the length of the list is 3 --> there are 3 strings in the list, 
# BUT, asking the code for the string at index 3 would through an error
# this is because string A is at index location 0, B is at 1 and C is at 2
# for this reason, we ask for the string at location lengthlist - 1, which =2
print(listofstrings[lengthlist-1])

# Bonus content: 
# list[-n] syntax gets the nth-to-last element,
# so list[-1] gets the last element, and list[-2] gets the second to last, etc.
# print the last element of the list, regardless of length of list
print (listofstrings[-1])

listintegers = [1, 5, 9]
# print(listintegers[0])

' For loops and Range '

# for loop examples
for i in range(1, 5):
    # starts counting at 1 because start specified
    print (i)

# line break that shows up as empty space in console
print ('\n')     

for i in range(5):
    # by default, starts count from 0 because start not specified
    # combining with if statements
    if i <= 2:
        None
    else:
        print (i)

FavNumbers = [1, 5, 1988]
for i in FavNumbers:
    x = i * 4
    print (x)

''' Adding and Removing from List '''

# create an empty list
new_list = []
# loop over a range of numbers from default starting value of 0 to 
# number in brackets, e.g., 5, subtract 1, e.g., here this would be 4
# each value of i (0, 1, 2, 3, and 4) are added (not mathematically) to list
for i in range(5):
    new_list.append(i)

print (new_list)
new_list.append('random string')
new_list.remove(2)

# print (new_list, new_list.index(3))

# if 3 in new_list:
#     print('this item is in the list')

''' Iterating Over Multiple Lists '''

new_list2 = [1, 3, 5, 6]
new_list3 = ['cat', 'dog', 'goose']

zipped_list = zip(new_list, new_list2)
print (zipped_list, '- this is the zipped list object')
print (list(zipped_list), '- this is the actual zipped list')

title_lists = ['list 1:', 'list 2:', 'list 3:']
all_lists = [new_list, new_list2, new_list3] 

# looping through both lists in order from 0th element to the last
# we don't have to use "i" and "j" notation below, but these are 
# pretty common to indicate the ith element of the first list and 
# jth element of the second list
# in this example, our second list, all_lists, is a list of lists
# so each jth element is itself a list!
for i, j in zip(title_lists, all_lists):
    print ('\n') # little line break to chill out the code spacing
    print (i, j, len(j), 'printing next element of each list')
    
    # adding in some list indexing stuff we learned above and
    # a quick little for loop
    if i == title_lists[-1]:
        print (
            '\n', # bit more line breaking so we can read easier
            'Phew, making sense of lists is a lot of work.', '\n',
            'Give yourself a round of applause *claps in circle above head*',
            '\n'
            )

for x, y, z in zip(new_list, new_list2, new_list3):
    print (x, y, z)

''' The Random Function '''
# random number from 0 to 10
print (random.randrange(10))
# random number from 0 to 9, min and max of range both specified
print (random.randint(0,9))

