

file = open("input.txt", "r")

result = 0


for line in file:
    nums = line.split()
    nums = [int(num) for num in nums]
    if nums[0] == nums[1]:
        continue
    increasing = True if nums[0] < nums[1] else False
    

    for i in range(0, len(nums) - 1):
        if increasing:
            if nums[i] >= nums[i + 1]:
                break
        else:
            if nums[i] <= nums[i + 1]:
                break

        if not 3>= abs(nums[i] - nums[i + 1]) >= 1:
            break
    else:
        result += 1
        print(nums)

print(result)