import copy
import time

plan = open("Day 6/input_demo.txt").readlines()

for i in range(len(plan)):
    plan[i] = plan[i].strip("\n")

loops = 0

history = {}

cursor = (None, None)
for y in range(len(plan)):
    for x in range(len(plan[y])):
        if plan[y][x] in ["^", ">", "v", "<"]:
            cursor = (y, x)
            break
    if cursor != (None, None):
        break
print(cursor)

start_time = time.time()
runs = 0
def step(plan, cursor, visited,count_loops = True, first_run = False):
    global loops
    global history
    global runs
    runs += 1
    #print("Cursor", cursor)
    #print("History", history)
    #print(f"-------{loops}---{count_loops}--------", visited)
    #for row in range(len(plan)):
    #    print(plan[row])

    #time.sleep(0.2)
    y, x = cursor

    
    if not count_loops and (y, x, plan[y][x]) in visited and not first_run:
        return True, cursor
    elif not count_loops and (y, x, plan[y][x]) in history:
        if history[(y, x, plan[y][x])]:
            return True, cursor
        else:
            raise Exception("Fake Out of bounds")
    else:
        new_cursor = copy.copy(cursor)
        possible_loop = copy.copy(plan)
        new_visited = copy.copy(visited)
    
    visited.add((y, x, plan[y][x]))

    if plan[y][x] == "^":
        if plan[y-1][x] in [".", "X", "-","|"]:
            if y == 0:
                raise Exception("Out of bounds")
            plan[y-1] = plan[y-1][:x] + "^" + plan[y-1][x+1:]
            cursor = (y-1, x)
            plan[y] = plan[y][:x] + "|" + plan[y][x+1:]
            if count_loops and possible_loop[y-2][x] == ".":
                possible_loop[y-2] = possible_loop[y-2][:x] + "#" + possible_loop[y-2][x+1:]
            else:
                count_loops = False
        else:
            plan[y] = plan[y][:x] + ">" + plan[y][x+1:]
            return plan, cursor
    elif plan[y][x] == ">":
        if plan[y][x+1] in [".", "X", "-","|"]:
            if x == len(plan[y]) - 1:
                raise Exception("Out of bounds")
            plan[y] = plan[y][:x] + "-" + plan[y][x+1:]
            cursor = (y, x+1)
            plan[y] = plan[y][:x+1] + ">" + plan[y][x+2:]
            if count_loops and possible_loop[y][x+2] == ".":
                possible_loop[y] = possible_loop[y][:x+2] + "#" + possible_loop[y][x+3:]
            else:
                count_loops = False
        else:
            plan[y] = plan[y][:x] + "v" + plan[y][x+1:]
            return plan, cursor
    elif plan[y][x] == "v":
        if plan[y+1][x] in [".", "X", "-","|"]:
            if y == len(plan) - 1:
                raise Exception("Out of bounds")
            plan[y+1] = plan[y+1][:x] + "v" + plan[y+1][x+1:]
            cursor = (y+1, x)
            plan[y] = plan[y][:x] + "|" + plan[y][x+1:]
            if count_loops and possible_loop[y+2][x] == ".":
                possible_loop[y+2] = possible_loop[y+2][:x] + "#" + possible_loop[y+2][x+1:]
            else:
                count_loops = False
        else:
            plan[y] = plan[y][:x] + "<" + plan[y][x+1:]
            return plan, cursor
    elif plan[y][x] == "<":
        if plan[y][x-1] in [".", "X", "-","|"]:
            if x == 0:
                raise Exception("Out of bounds")
            plan[y] = plan[y][:x-1] + "<" + plan[y][x:]
            cursor = (y, x-1)
            plan[y] = plan[y][:x] + "-" + plan[y][x+1:]
            if count_loops and possible_loop[y][x-2] == ".":
                possible_loop[y] = possible_loop[y][:x-2] + "#" + possible_loop[y][x-1:]
            else:
                count_loops = False
        else:
            plan[y] = plan[y][:x] + "^" + plan[y][x+1:]
            return plan, cursor

    if count_loops:
        in_bounds = True

        minihistory = []
        while in_bounds:
            try:
                key = (new_cursor[0], new_cursor[1], plan[new_cursor[0]][new_cursor[1]])
                minihistory.append(key)
                #if key not in history:
                possible_loop, new_cursor = step(possible_loop, new_cursor, new_visited, count_loops = False)
                #else:
                #    if history[key]:
                #        loops += 1
                #        print(round(time.time()-start_time),"seconds: loop found", loops)
                #    break
                if type(possible_loop) == bool and possible_loop == True:
                    loops += 1
                    print(round(time.time()-start_time),"seconds: loop found", loops)
                    for i in range(3,len(minihistory)):
                        history[minihistory[i]] = True
                    break
            except Exception as e :
                #print(e)
                in_bounds = False
                for i in range(1,len(minihistory)):
                    history[minihistory[i]] = False

    return plan, cursor

in_bounds = True
solution = 0
count_loops = False
visited = set()
while in_bounds:
    try:
        plan, cursor = step(plan, cursor, visited, count_loops=True, first_run=not count_loops)
        count_loops = True
    except:
        in_bounds = False
        
print(loops)
print(runs)