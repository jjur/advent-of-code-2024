import re

file = open("Day3/input.txt", "r").read()
commands=re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", str(file))

result = 0
write_mode = True
for command in commands:
    if command == "do()":
        write_mode = True
    elif command == "don't()":
        write_mode = False
    else:
        if write_mode:
            
            command = command.replace("mul(", "").replace(")", "")
            a,b = command.split(",")
            result += int(a) * int(b)

print(result)