import re

with open("input.txt") as day11input:
    row_list = [x.strip() for x in day11input.readlines()]

row_list = row_list
history = row_list[:]
change_flag = True
changept2 = True

def check_seat(row, col):
    # check all 8 options for row column 
    global change_flag
    conflict = 0
    str_list = list(history[row])
    self = str_list[col]
    row_min = 0 if row == 0 else row - 1
    row_max = row if row == len(row_list) - 1 else row + 1
    col_min = 0 if col == 0 else col - 1
    col_max = col if col == len(str_list) - 1 else col + 1
    for check_row in range(row_min, row_max + 1):
        for check_col in range(col_min, col_max + 1):
            if not (row == check_row and col == check_col):
                if(history[check_row][check_col] == "#"):
                    conflict = conflict + 1
                if(conflict >= 4 and self == "#"):
                    change_flag = True
                    return "L"
    if(conflict == 0 and self == "L"):
        change_flag = True
        return "#"
    return self

def configure_row(row, index):
    col_index = 0
    row_list = list(row)
    for letter in row:
        if not (letter == "."):
            row_list[col_index] = check_seat(index, col_index)
        col_index = col_index + 1
    return "".join(row_list)


#while(change_flag):
 #   row_index = 0
  #  change_flag = False
   # history = row_list[:]
    #for row in row_list:
     #   row_list[row_index] = configure_row(row, row_index)
      #  row_index = row_index + 1
#print(sum(sum(letter in '#' for letter in row) for row in row_list))

def check_seat_recursion(row_index, col_index, direction):
    # direction from 0 W, NW, N, NE, E, SE, S, SW
    if not (row_index in range(0, len(row_list)) and col_index in range(0, len(row_list[row_index]))):
        return "."

    self = history[row_index][col_index]
    if(self == "."):
        if(direction == "W"):
            return check_seat_recursion(row_index, col_index - 1, direction)
        if(direction == "E"):
            return check_seat_recursion(row_index, col_index + 1, direction)
        if(direction == "N"):
            return check_seat_recursion(row_index - 1, col_index, direction)
        if(direction == "S"):
            return check_seat_recursion(row_index + 1, col_index, direction)
        if(direction == "NW"):
            return check_seat_recursion(row_index - 1, col_index - 1, direction)
        if(direction == "SW"):
            return check_seat_recursion(row_index + 1, col_index - 1, direction)
        if(direction == "NE"):
            return check_seat_recursion(row_index - 1, col_index + 1, direction)
        if(direction == "SE"):
            return check_seat_recursion(row_index + 1, col_index + 1, direction)
    return self

def check_seat_pt2(row, col):
    global changept2
    conflict = 0
    str_list = list(history[row])
    self = str_list[col]
    tup = []
    tup.append(check_seat_recursion(row, col - 1, "W"))
    tup.append(check_seat_recursion(row - 1, col - 1, "NW"))
    tup.append(check_seat_recursion(row - 1, col, "N"))
    tup.append(check_seat_recursion(row - 1, col + 1, "NE"))
    tup.append(check_seat_recursion(row, col + 1, "E"))
    tup.append(check_seat_recursion(row + 1, col + 1, "SE"))
    tup.append(check_seat_recursion(row + 1, col, "S"))
    tup.append(check_seat_recursion(row + 1, col - 1, "SW"))
    conflict = sum(x in "#" for x in tup)
    # print("Row: " + str(row) + " Col: " + str(col) + " tuple: " + str(tup)) + " conflict: " + str(conflict)
    if(conflict == 0 and self == "L"):
        changept2 = True
        return "#"
    if(conflict >= 5):
        changept2 = True
        return "L"
    return self

def configure_row_pt2(row, index):
    col_index = 0
    row_list = list(row)
    for letter in row:
        if not (letter == "."):
            row_list[col_index] = check_seat_pt2(index, col_index)
        col_index = col_index + 1
    return "".join(row_list)


while(changept2):
# for i in range(0,7):
    row_index = 0
    changept2 = False
    # print(history)
    history = row_list[:]
    for row in row_list:
        row_list[row_index] = configure_row_pt2(row, row_index)
        row_index = row_index + 1
print(sum(sum(letter in '#' for letter in row) for row in row_list))
