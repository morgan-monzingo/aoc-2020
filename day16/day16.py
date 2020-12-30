with open("input.txt") as dayinput:
    puzzle_input_lines = [x for x in dayinput.readlines()]

def create_boundaries(line, field_values):
    colon = line.strip().split(":")
    # print(colon)
    space_input = colon[1].strip().split(" ")
    # print(space_input)
    tup_1 = space_input[0].strip().split("-")
    # print(tup_1)
    tup_2 = space_input[2].strip().split("-")
    # print(tup_2)
    field_values.append((int(tup_1[0]),int(tup_1[1])))
    field_values.append((int(tup_2[0]),int(tup_2[1])))
    return field_values


def process_ticket(ticket, field_values):
    ticket_val = ticket.strip().split(",")
    result = []
    for val_str in ticket_val:
        val = int(val_str)
        # print("checking val: " + val_str)
        if not any(lower <= val <= upper in (lower, upper) for (lower, upper) in field_values):
            return []
    return ticket_val

def categorize_ticket(ticket, field_values, final_matches):
    for index in range(0,len(ticket)):
        tup_index = 0
        for (lower, upper)  in field_values:
            # print("Comparing: " + str(lower) + " " + str(ticket[index]) + " " + str(upper))
            if(lower <= int(ticket[index]) <= upper):
                try:
                    # print("true for spot: " + str(tup_index//2) + " " + str(index))
                    final_matches[tup_index//2][index] = final_matches[tup_index//2][index] + 1
                except KeyError as e:
                    final_matches[tup_index//2] = [0 for x in ticket]
                    final_matches[tup_index//2][index] = final_matches[tup_index//2][index] + 1
                    pass
            tup_index  = tup_index + 1
    # print(final_matches)
    return final_matches

def process_list(final_matches, ticket_len):
    single_match = [-1 for x in final_matches.items()]
    for key in final_matches.keys():
        final_matches[key] = [tup[0] for tup in list(enumerate(final_matches[key])) if tup[1] == ticket_len]
        list_tup = final_matches[key]
        if len(list_tup) == 1:
            print("the tuple is 1")
            print(list_tup)
            single_match[key] = list_tup[0]
            print(single_match[key])
            print(key)
            print(single_match)
            del(final_matches[key])
        print(single_match)

    while(any(k == -1 for k in single_match)):
        for key in final_matches.keys():
            print("in for loop")
            print(final_matches[key])
            updated_match  = [x for x in final_matches[key] if x not in single_match]
            print(updated_match)
            final_matches[key] = updated_match
            if len(updated_match) == 1:
                single_match[key] = updated_match[0]
                del(final_matches[key])
    return single_match

    
def process_input(puzzle_input):
    field_values = []
    line = puzzle_input.pop(0)
    # print("Line step 1 0: " + line)
    while not(line == '\n'):
        field_values = create_boundaries(line, field_values)
        line = puzzle_input.pop(0)
        # print("Line step 1: " + line)
    # print(field_values)
    line = puzzle_input.pop(0)
    # print("Line step 2 0: " + line)
    your_ticket = puzzle_input.pop(0)
    puzzle_input.pop(0)
    line = puzzle_input.pop(0) # should be "nearby tickets: 
    # print("Line step 3 0: " + line)
    index = 0
    # remove the invalid tickets
    valid_tickets = []
    for ticket in puzzle_input:
        checked_ticket = process_ticket(ticket, field_values)
        if not (checked_ticket == []):
            valid_tickets.append(checked_ticket)
    final_matches = {}
    for ticket in valid_tickets:
        final_matches = categorize_ticket(ticket, field_values, final_matches)
    tickets = process_list(final_matches, len(valid_tickets))
    tickets = tickets[:6]
    product = 1
    ticket_val = your_ticket.split(",")
    for spot in tickets:
        product = product * int(ticket_val[spot])
    return product
            

print(process_input(puzzle_input_lines))


