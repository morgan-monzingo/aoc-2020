day_inputs = open('input.txt', 'r')
inputs_list = day_inputs.readlines()
index = 0
num_trees = 0

for i in inputs_list:
    if i[index] == '#':
        num_trees += 1
    index += 3
    if (index > len(i)-2):
        index -= len(i)-1

print(num_trees)

day_inputs.close()

day_inputs = open('input.txt', 'r')
inputs_list = day_inputs.readlines()
single_step_slope_depths = [1, 3, 5, 7]
double_step_slope_depths = [1]
found_trees_array = []

for slope_depth in single_step_slope_depths:
    index = 0
    num_trees = 0
    for i in inputs_list:
        if i[index] == '#':
            num_trees += 1
        index += slope_depth
        if (index > len(i)-2):
            index -= len(i)-1
    found_trees_array.append(num_trees)

for slope_depth in double_step_slope_depths:
    index = 0
    num_trees = 0
    should_count_row = True
    for i in inputs_list:
        if should_count_row and i[index] == '#':
            num_trees += 1
            index += slope_depth
            if (index > len(i)-2):
                index -= len(i)-1
        should_count_row = not should_count_row
    found_trees_array.append(num_trees)

num_total_trees = long(1)
for tree_count in found_trees_array:
    num_total_trees *= long(tree_count)

print(num_total_trees)

day_inputs.close()
