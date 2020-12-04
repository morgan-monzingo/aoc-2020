import re

with open("input.txt") as day2input:
    password_list = [x.strip() for x in day2input.readlines()]

def is_password_invalid(entry):
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
            return 1
    if(match < minAmt):
        return 1
    return 0

print(sum(is_password_invalid(entry) for entry in password_list))


