import re
from itertools import product

with open("input.txt") as dayinput:
    puzzle_input_lines = [x.strip() for x in dayinput.readlines()]

turn_count = {}

def calculate_new_value(previous, turn):
    global turn_count
    diff = 0
    # print(turn_count[str(previous)])
    if(len(turn_count[str(previous)]) >= 2):
        last_turn_1 = turn_count[str(previous)][-1]
        last_turn_2 = turn_count[str(previous)][-2]
        diff = last_turn_1 - last_turn_2
    try:
        turn_count[str(diff)].append(turn)
    except KeyError as e:
        turn_count[str(diff)] = [turn]
        pass
    return diff
    
    
def process_input(puzzle_input):
    global turn_count
    turn_count = {k: [v] for v, k in enumerate(puzzle_input)}
    previous = puzzle_input[-1]
    # for turn in range(len(puzzle_input),2020):
    for turn in range(len(puzzle_input),30000000):
        # print(turn_count)
        # print("previous val: " + str(previous))
        previous = calculate_new_value(previous, turn)
    return previous

print(process_input(puzzle_input_lines[0].split(',')))


