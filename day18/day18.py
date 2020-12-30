with open("input.txt") as dayinput:
    puzzle_input_lines = [x for x in dayinput.readlines()]

def multiply(total, val):
    return total * val

def add(total, val):
    return total + val

def inner_exp(line, next_index):
    # know we just had an open or start of list 
    total = 0
    curr_op = ""

    print line
    while not next_index >= len(line):
        character = line[next_index - 1]
        print("start")
        print(character)
        print(next_index)
        if character.isdigit() and curr_op == "":
            print("number")
            total = int(character)
            next_index = next_index + 1
        if character.isdigit() and curr_op == "*":
            print("multiply")
            total = multiply(total, int(character))
            next_index = next_index + 1
        if character.isdigit() and curr_op == "+":
            print("add")
            total = add(total, int(character))
            next_index = next_index + 1
        if character == "(":
            print("open paran")
            (inner, nxt)  = inner_exp(line[next_index:], 1)
            print(inner)
            print(nxt)
            next_index = nxt + next_index 
            print("next index after inner " + str(next_index))
            if curr_op == "*":
                print("multiply")
                total = multiply(total, inner)
            if curr_op == "+":
                print("add")
                total = add(total, inner)
            if curr_op == "": 
                total = inner
        if character == ")":
            print("close " + str(total) + " " + str(next_index + 1))
            next_index = next_index + 1
            return (total, next_index)
        if character == "*" or character == "+":
            print("op")
            curr_op = character
            next_index = next_index + 1
        print("current total" + str(total))
    return (total, next_index)

print(sum(inner_exp(list(line.replace(" ", "")), 1)[0] for line in puzzle_input_lines ))


