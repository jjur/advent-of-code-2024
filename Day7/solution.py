
input = open("Day7/input.txt").readlines()

def solve(input, target):
    if len(input) == 1:
        return input[0] == target
    
    sum_part = input[0] + input[1]
    multiply_part = input[0] * input[1]
    new_input = input[2:]
    return solve([sum_part] + new_input, target) or solve([multiply_part] + new_input, target)
    


correct = 0
for i in range(len(input)):
    input[i] = input[i].strip("\n")
    result = int(input[i].split(": ")[0])
    inputs = input[i].split(": ")[1].strip().split(" ")
    inputs = [int(x) for x in inputs]
    if solve(inputs, result):
        correct += result
        print("pass", result)

print(correct)


