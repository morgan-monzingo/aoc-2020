import re
from itertools import product

with open("input.txt") as dayinput:
    puzzle_input_lines = [x.strip() for x in dayinput.readlines()]

def calculate_new_value(value, mask):
    comparison = zip(value, mask)
    val = []
    for entry in comparison:
        if entry[1] == "X":
            val.append(entry[0])
        else:
            val.append(entry[1])
    return int(''.join(val), 2)

def calculate_index_list(value, mask):
    # repeat the number of X that we have in the value
    comparison = zip(value, mask)
    x_count = 0
    val = []
    index_list = []
    for entry in comparison:
        # print(entry)
        if entry[1] == "X":
            x_count = x_count + 1
            val.append(entry[1])
        elif entry[1] == "0":
            val.append(entry[0])
        else:
            val.append(entry[1])
    combos = product(range(2), repeat=x_count)
    for combo in combos:
        index = "".join(val)
        for bit in combo:
            index = index.replace("X", str(bit), 1)
        print(index)
        index_list.append(int(index, 2))
    return index_list


def process_input(puzzle_input):
    mask = ""
    results = {}
    for entry in puzzle_input:
        if(entry[0:4] == "mask"):
            mask = entry[7:]
        else:
            raw_entry = int(entry.split('=')[1])
            bin_val = '{0:036b}'.format(raw_entry)
            key = str(re.search(r"\[([0-9_]+)\]", entry).group(1))
            results[key] = calculate_new_value(bin_val,mask)
    return results

def process_pt2_input(puzzle_input):
    mask = ""
    results = {}
    for entry in puzzle_input:
        if(entry[0:4] == "mask"):
            mask = entry[7:]
        else:
            raw_entry = int(entry.split('=')[1])
            key = int(re.search(r"\[([0-9_]+)\]", entry).group(1))
            print("key" + str(key))
            index_val = '{0:036b}'.format(key)
            print("new index: " + str(index_val))
            index_list = calculate_index_list(index_val,mask)
            # print("index list ****************************")
            # print(index_list)
            for index in index_list:
                results[index] = raw_entry
    print(results)
    return results

# print(sum(process_input(puzzle_input_lines).values()))
print(sum(process_pt2_input(puzzle_input_lines).values()))

