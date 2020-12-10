import re

with open("input.txt") as day5input:
    seat_list = [x.strip() for x in day5input.readlines()]

def calculate_seat_id(seat_code):
    row_max = 127
    row_min = 0
    row = 0
    seat_max = 7
    seat_min = 0
    seat = 0
    for letter in seat_code:
        if(letter == "B" or letter == "F"):
            row_range = (row_max - row_min + 1)/2
            if(row_range > 1):
                if(letter == "B"):
                    row_min = row_min + row_range
                if(letter == "F"):
                    row_max = row_max - row_range
            else:
                if(letter == "B"):
                    row = row_max
                else:
                    row = row_min
        else:
            seat_range = (seat_max - seat_min + 1)/2
            if(seat_range > 1):
                if(letter == "R"):
                    seat_min = seat_min + seat_range
                if(letter == "L"):
                    seat_max = seat_max - seat_range
            else:
                if(letter == "R"):
                    seat = seat_max
                else:
                    seat = seat_min
    return (row * 8 + seat)

def calculate_self_seat(seat_list):
    for seat in range(min(seat_list),max(seat_list)):
        if(seat in seat_list):
            next
        else:
            if((seat-1) in seat_list and (seat + 1) in seat_list):
                return seat
    return 0

print(max(calculate_seat_id(entry) for entry in seat_list))
print(calculate_self_seat(sorted(calculate_seat_id(entry) for entry in seat_list)))
