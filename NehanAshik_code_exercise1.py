'''
Created on 23 Sept 2026

@author: nehan
'''

import random

#creating lists with courses and  adjectives
fav_courses = ['Calculus 1', 'Fluid Mechanics', 'Calculus 2']
adjectives = ['good', 'great']

len_courses = len(fav_courses)
len_adjectives = len(adjectives)

#retrieving a random course and adjective
rand_course = fav_courses[random.randint(0,len_courses-1)]
rand_adjective = adjectives[random.randint(0,len_adjectives-1)]

#assigning a variable to the length of the shortest list
if len_courses < len_adjectives:
    smallestlistlen = len_courses
else:
    smallestlistlen = len_adjectives

fillerlist = ['is'] * smallestlistlen

#printing the combination of course with adjective
for sentence in zip(fav_courses, fillerlist, adjectives):
    for word in sentence:
        print(word, end=' ')
    print()

print("But my favourite course is", rand_course,"because it is very", rand_adjective)
