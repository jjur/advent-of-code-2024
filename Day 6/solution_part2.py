import copy
import time

plan = open("Day 6/input.txt").readlines()

for i in range(len(plan)):
    plan[i] = plan[i].strip("\n")

loops = 0

start_time = time.time()
def step(plan, visited,count_loops = True, first_run = False):
    global loops

    #print(f"-------{loops}---{count_loops}--------", visited)
    #for row in range(len(plan)):
    #    print(plan[row])

    #time.sleep(0.2)

    
    for y in range(len(plan)):
        for x in range(len(plan[y])):
            if plan[y][x] in ['.', '#', "X", "-","|"]:
                continue
            
            if not count_loops and (x, y,plan[y][x]) in visited and not first_run:
                return True 
            else:
                possible_loop = copy.deepcopy(plan)
                new_visited = copy.deepcopy(visited)
            
            visited.add((x, y, plan[y][x]))

            if plan[y][x] == "^":
                if plan[y-1][x] in [".", "X", "-","|"]:
                    if y == 0:
                        raise Exception("Out of bounds")
                    plan[y-1] = plan[y-1][:x] + "^" + plan[y-1][x+1:]
                    plan[y] = plan[y][:x] + "|" + plan[y][x+1:]
                    if count_loops and possible_loop[y-2][x] == ".":
                        possible_loop[y-2] = possible_loop[y-2][:x] + "#" + possible_loop[y-2][x+1:]
                    else:
                        count_loops = False
                else:
                    plan[y] = plan[y][:x] + ">" + plan[y][x+1:]
                    return plan
            elif plan[y][x] == ">":
                if plan[y][x+1] in [".", "X", "-","|"]:
                    if x == len(plan[y]) - 1:
                        raise Exception("Out of bounds")
                    plan[y] = plan[y][:x] + "-" + plan[y][x+1:]
                    plan[y] = plan[y][:x+1] + ">" + plan[y][x+2:]
                    if count_loops and possible_loop[y][x+2] == ".":
                        possible_loop[y] = possible_loop[y][:x+2] + "#" + possible_loop[y][x+3:]
                    else:
                        count_loops = False
                else:
                    plan[y] = plan[y][:x] + "v" + plan[y][x+1:]
                    return plan
            elif plan[y][x] == "v":
                if plan[y+1][x] in [".", "X", "-","|"]:
                    if y == len(plan) - 1:
                        raise Exception("Out of bounds")
                    plan[y+1] = plan[y+1][:x] + "v" + plan[y+1][x+1:]
                    plan[y] = plan[y][:x] + "|" + plan[y][x+1:]
                    if count_loops and possible_loop[y+2][x] == ".":
                        possible_loop[y+2] = possible_loop[y+2][:x] + "#" + possible_loop[y+2][x+1:]
                    else:
                        count_loops = False
                else:
                    plan[y] = plan[y][:x] + "<" + plan[y][x+1:]
                    return plan
            elif plan[y][x] == "<":
                if plan[y][x-1] in [".", "X", "-","|"]:
                    if x == 0:
                        raise Exception("Out of bounds")
                    plan[y] = plan[y][:x-1] + "<" + plan[y][x:]
                    plan[y] = plan[y][:x] + "-" + plan[y][x+1:]
                    if count_loops and possible_loop[y][x-2] == ".":
                        possible_loop[y] = possible_loop[y][:x-2] + "#" + possible_loop[y][x-1:]
                    else:
                        count_loops = False
                else:
                    plan[y] = plan[y][:x] + "^" + plan[y][x+1:]
                    return plan

            if count_loops:
                in_bounds = True
                while in_bounds:
                    try:
                        new_plan = step(possible_loop, new_visited, count_loops = False)
                        if type(new_plan) == bool and new_plan == True:
                            loops += 1
                            print(round(time.time()-start_time),"seconds: loop found", loops)
                            break
                    except Exception as e :
                        print(e)
                        in_bounds = False

            return plan

in_bounds = True
solution = 0
count_loops = False
visited = set()
while in_bounds:
    try:
        plan = step(plan, visited, count_loops=True, first_run=not count_loops)
        count_loops = True
    except:
        in_bounds = False
        
        for row in plan:
            solution += row.count("X")

print(solution)
        