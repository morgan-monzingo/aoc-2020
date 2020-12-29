day_inputs = open('input.txt', 'r')
inputs_list = day_inputs.readlines()
xmas_data = []
preamble_length = 25

for i in inputs_list:
    if i != "\n":
        xmas_data.append(int(i))

start_index = 0
check_points = xmas_data[preamble_length:len(xmas_data)]

for data_point in check_points:
    xmas_data_subset = xmas_data[start_index:(start_index+preamble_length)]
    s = set()

    found_pair = False
    for i in range(0, preamble_length):
        temp = data_point-xmas_data_subset[i]
        if (temp in s):
            found_pair = True
        s.add(xmas_data_subset[i])

    if not found_pair:
        print(data_point)
        break

    start_index += 1

day_inputs.close()

day_inputs = open('input.txt', 'r')
inputs_list = day_inputs.readlines()
xmas_data = []

for i in inputs_list:
    if i != "\n":
        xmas_data.append(int(i))

sum_values = []
invalid_data_point = 41682220
test_sum = 0

for data_point in xmas_data:
    sum_values.append(data_point)
    test_sum += data_point

    while test_sum > invalid_data_point:
        test_sum -= sum_values[0]
        del sum_values[0]

    if test_sum == invalid_data_point:
        sum_values.sort()
        high_low_sum = sum_values[0] + sum_values[len(sum_values)-1]
        print(high_low_sum)
        break

day_inputs.close()
