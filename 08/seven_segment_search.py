'''Fixing broken seven segment displays i think'''

import pprint
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


'''
Three letters = 7
Two letters = 1
Four letters = 4
Seven letters = 8
'''

# For each input i should start with an empy dict of the possible wires

# Get and ready the input
puzzle = []
input = []

with open('./08/input.txt', "r") as file:
    lines = file.readlines()
    for l in lines:
        index = l.index('|')
        puzzle.append(l[:index])
        input.append(l[index + 2: -1])

template = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[]}

zero = ['a','b','c','e','f','g']
one = ['c','f']
two = ['a','c','d','e','g']
three = ['a','c','d','f','g']
four = ['b','c','d','f']
five = ['a','b','d','f','g']
six = ['a','b','d','e','f','g']
seven = ['a','c','f']
eight = ['a','b','c','d','e','f','g']
nine = ['a','b','c','d','f','g']

puzzle_values = puzzle[0].split()
for i in puzzle_values:
    if len(i) == 2:
        logging.debug('Letter is one')
    else:
        pass

