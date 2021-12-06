'''
Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. 
Numbers are chosen at random, and the chosen number is marked on all boards on which it appears.
 (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, 
 that board wins. (Diagonals don't count.)
'''

import pprint
import random
from typing import final

inputs = [
    [22, 13, 17, 11,  0,
    8,  2, 23,  4, 24,
    21,  9, 14, 16,  7,
    6, 10,  3, 18,  5,
    1, 12, 20, 15, 19],
    [3, 15,  0,  2, 22,
    9, 18, 13, 17,  5,
    19,  8,  7, 25, 23,
    20, 11, 10, 24,  4,
    14, 21, 16, 12,  6],
    [14, 21, 17, 24,  4,
    10, 16, 15,  9, 19,
    18,  8, 23, 26, 20,
    22, 11, 13,  6,  5,
    2,  0, 12,  3,  7]
]

#generate boards

#boards will be a dict index will be position on grid, value will be list 
# First item will be actual, second will be bool

def create_bingo_grid(list_nums,name):
    '''Create bingo grid dict from num list'''
    grid = {}
    grid['gridno'] = num
    loop_value = 0
    for i in range(5):
        for j in range(5):
            grid[tuple([i,j])] = [list_nums[loop_value],False]
            loop_value += 1
    # pprint.pprint(grid)
    return grid

def mark_number(n,grid):
    '''Mark numbers on grid as True if present'''
    copy = grid.copy()
    key_list = list(grid.keys())
    values_list = list(grid.values())

    position = values_list.index([n,False])
    key = key_list[position]
    grid[key] = [n,True]
    return copy
    # for key, number in enumerate(list_nums):

def check_grid(n, grids):
    '''Check each grid for number'''
    for grid in grids:
        if [n,False] in grid.values():
            grid = mark_number(n,grid)

def call_number(i,grids):
    '''Emulate a numbers called in bingo'''
    check_grid(i,grids)

def check_grids_for_winner(grid):
    '''Check for a row or a column to all be marked "True"'''
    #Check Rows
    for row in range(5):
        this_row = []
        for j in range(5):
            if grid[(row,j)][1] == True:
                this_row.append(grid[(row,j)][0])
        if len(this_row) == 5:
            return ["Won", sum(this_row), grid['gridno']]
    #Check Columns
    for column in range(5):
        this_row = []
        for j in range(5):
            if grid[(j,column)][1] == True:
                this_row.append(grid[(row,j)][0])
        if len(this_row) == 5:
            return ["Won", sum(this_row)]
    return ["No Win", 0]
        
final_score = 0
max_number = 0

for i in inputs:
    for number in i:
        if number > max_number:
            max_number = number

grids = []

for num,sets in enumerate(inputs):
    grids.append(create_bingo_grid(sets,num))

game_running = True
round = 0
while game_running:
    if round > 40:
        print("Round Limit Exceeded")
        break
    number = random.randint(0,max_number)
    call_number(number,grids)


    for grid in grids:
        if game_running == True:
            result= check_grids_for_winner(grid)
            if result[0] == "Won":
                number_called_at_win = number
                values = list(grid.values())[1:]
                total = 0
                for i in values:
                    if i[1] == True:
                        total += i[0]
                final_score = total * number_called_at_win
                
                    
                game_running = False
                break
        elif game_running == False:
            break
    round += 1

print("results")
print(final_score)





