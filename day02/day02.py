import re

with open("input.txt") as day2input:
    password_list = [x.strip() for x in day2input.readlines()]

def is_password_valid(entry):
    tup = re.split('-| |:', entry)
    minAmt = int(tup[0])
    maxAmt = int(tup[1])
    code = tup[2]
    password = tup[4]
    match = 0
    for letter in password:
        if(letter == code):
            match+=1
        if(match > maxAmt):
            return 0
    if(match < minAmt):
        return 0
    return 1

def pt2_is_password_valid(entry):
    tup = re.split('-| |:', entry)
    pos1 = int(tup[0]) - 1
    pos2 = int(tup[1]) - 1
    code = tup[2]
    password = tup[4]
    if((password[pos1] == code and password[pos2] != code) or (password[pos1] != code and password[pos2] == code)):
        return 1
    return 0

print(sum(is_password_valid(entry) for entry in password_list))

print(sum(pt2_is_password_valid(entry) for entry in password_list))

