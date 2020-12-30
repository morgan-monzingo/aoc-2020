with open("input.txt") as day_input:
    puzzle_list = [int(x.strip()) for x in day_input.readlines()]

def find_values(puzzle_input):
    puzzle_input.sort()
    input_sum = 2020
    for front in puzzle_input:
        for back in reversed(puzzle_input):
            sum_val = front + back
            if sum_val  == input_sum:
                return (front, back)
            elif sum_val < input_sum:
                break

def find_three_values(puzzle_input):
    puzzle_input.sort()
    input_sum = 2020
    for front in puzzle_input:
        for back in reversed(puzzle_input):
            if front + back < input_sum:
                for second in reversed(puzzle_input):
                    sum_val = front + back + second
                    if sum_val  == input_sum:
                        return (front, back, second)
                    elif sum_val < input_sum:
                        break

(x,y) = find_values(puzzle_list)
print x*y

(x,y,z) = find_three_values(puzzle_list)
print find_three_values(puzzle_list)
print x*y*z

