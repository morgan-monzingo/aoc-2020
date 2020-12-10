import re

with open("input.txt") as day8input:
    step_list = [x.strip() for x in day8input.readlines()]

step_list = step_list
hit_list = [False for i in step_list]
history = step_list[:]
switch_steps = [step.split( )[0] for step in step_list]

def process_line(index, acc):
        global hit_list
        global step_list
        if(index == len(step_list)):
            print(str(acc))
            return acc
        step = step_list[index]
        tup = step.split( )
        if(hit_list[index] == True):
            hit_list = [False for i in hit_list]
            return -1
        hit_list[index] = True
        if(tup[0] == "nop"):
            return process_line(index + 1, acc)
        if(tup[0] == "jmp"):
            val = tup[1][1:]
            if(tup[1][0] == "-"):
                return process_line(index - int(val), acc)
            return process_line(index + int(val), acc)
        if(tup[0] == "acc"):
            val = tup[1][1:]
            if(tup[1][0] == "-"):
                acc = acc - int(val)
            else:
                acc = acc + int(val)
            return process_line(index + 1, acc)

def process_bug():
    acc = process_line(0,0)
    print(acc)

def process_bug():
    global step_list
    index = 0
    switch_index = []
    for step in switch_steps:
        if(step == "jmp" or step == "nop"):
            switch_index.append(index)
        index = index + 1
    ret_val = -1
    for index in switch_index:
        if(ret_val == -1):
            step_list = history[:]
            old_cmd = switch_steps[index]
            if(old_cmd == "nop"):
                step_list[index] = step_list[index].replace("nop", "jmp")
            else:
                step_list[index] = step_list[index].replace("jmp", "nop")
        else: 
            print(ret_val)
        ret_val = process_line(0,0)

process_bug()

