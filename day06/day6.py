day_inputs = open('input.txt', 'r')
inputs_list = day_inputs.readlines()
array_yes_sets = []
yes_set = set()

for i in inputs_list:
    for j in i:
        if j != "\n":
            yes_set.add(j)
    if i == "\n":
        array_yes_sets.append(yes_set)
        yes_set = set()

array_yes_sets.append(yes_set)

total_yes = 0
for found_yes_set in array_yes_sets:
    total_yes += len(found_yes_set)

print(total_yes)

day_inputs.close()

day_inputs = open('input.txt', 'r')
inputs_list = day_inputs.readlines()
array_yes_sets = []
base_yes_set = set()
comparison_yes_set = set()
first_set = True
all_yes = True

for i in inputs_list:
    for j in i:
        if j != "\n":
            if first_set:
                base_yes_set.add(j)
            else:
                comparison_yes_set.add(j)
    first_set = False

    if len(comparison_yes_set) != 0:
        base_yes_set = base_yes_set.intersection(comparison_yes_set)
        if len(base_yes_set) == 0:
            all_yes = False

    comparison_yes_set = set()
    if i == "\n":
        if all_yes:
            array_yes_sets.append(base_yes_set)
        first_set = True
        all_yes = True
        base_yes_set = set()
        comparison_yes_set = set()

if all_yes:
    array_yes_sets.append(base_yes_set)

total_yes = 0
for found_yes_set in array_yes_sets:
    total_yes += len(found_yes_set)

print(total_yes)

day_inputs.close()
