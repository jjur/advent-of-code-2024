import  random
import time

rules = []
updates = []
with open('input.txt', "r") as f:
    reading_rules = True
    for line in f:
        line = line.strip()
        if line == "":
            reading_rules = False
            continue
        if reading_rules:
            rules.append(tuple(line.split("|")))
        else:
            updates.append(line.split(","))


valid_updates = []
invalid_updates = []

def is_valid(update, rules):
    for rule in rules:
        num1, num2 = rule
        try:
            pos1, pos2 = update.index(num1), update.index(num2)
        except ValueError:
            continue

        if pos1 >= pos2:
            return False
    return True

for update in updates:
    for rule in rules:
        num1, num2 = rule
        try:
            pos1, pos2 = update.index(num1), update.index(num2)
        except ValueError:
            continue

        if pos1 >= pos2:
            invalid_updates.append(update)
            break


start_time = time.time()
for update in invalid_updates:
    while not is_valid(update, rules):
        random.shuffle(update)

    print(time.time()-start_time,"fixed",update)

print(invalid_updates)
solution = 0
for update in invalid_updates:
    l = len(update)//2
    solution += int(update[l])

print(solution)

