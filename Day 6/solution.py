
plan = open("input.txt").readlines()

def step():
    global plan
    for y in range(len(plan)):
        for x in range(len(plan[y])):
            if plan[y][x] in ['.', '#', "X"]:
                continue

            if plan[y][x] == "^":
                if plan[y-1][x] in [".", "X"]:
                    if y == 0:
                        raise Exception("Out of bounds")
                    plan[y-1] = plan[y-1][:x] + "^" + plan[y-1][x+1:]
                    plan[y] = plan[y][:x] + "X" + plan[y][x+1:]
                else:
                    plan[y] = plan[y][:x] + ">" + plan[y][x+1:]
            elif plan[y][x] == ">":
                if plan[y][x+1] in [".", "X"]:
                    if x == len(plan[y]) - 1:
                        raise Exception("Out of bounds")
                    plan[y] = plan[y][:x] + "X" + plan[y][x+1:]
                    plan[y] = plan[y][:x+1] + ">" + plan[y][x+2:]
                else:
                    plan[y] = plan[y][:x] + "v" + plan[y][x+1:]
            elif plan[y][x] == "v":
                if plan[y+1][x] in [".", "X"]:
                    if y == len(plan) - 1:
                        raise Exception("Out of bounds")
                    plan[y+1] = plan[y+1][:x] + "v" + plan[y+1][x+1:]
                    plan[y] = plan[y][:x] + "X" + plan[y][x+1:]
                else:
                    plan[y] = plan[y][:x] + "<" + plan[y][x+1:]
            elif plan[y][x] == "<":
                if plan[y][x-1] in [".", "X"]:
                    if x == 0:
                        raise Exception("Out of bounds")
                    plan[y] = plan[y][:x-1] + "<" + plan[y][x:]
                    plan[y] = plan[y][:x] + "X" + plan[y][x+1:]
                else:
                    plan[y] = plan[y][:x] + "^" + plan[y][x+1:]
            return plan

in_bounds = True
solution = 0
while in_bounds:
    try:
        plan = step()
    except:
        in_bounds = False
        
        for row in plan:
            solution += row.count("X")

print(solution)
        