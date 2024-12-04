import re

file = open("Day3/input.txt", "r").read()
commands=re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', str(file))

result = 0
for command in commands:
    command = command.replace("mul(", "").replace(")", "")
    a,b = command.split(",")
    result += int(a) * int(b)

print(result)