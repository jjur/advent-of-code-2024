

file = open("Day2/input.txt", "r")

result = 0
solutions = []

def verify_nums(nums, increasing=None, damepenr_used=False):
    if increasing is None:
        increasing = True if nums[0] < nums[1] else False
    
    for i in range(0, len(nums) - 1):
        err = False
        if increasing:
            if nums[i] >= nums[i + 1]:
                err = True
        else:
            if nums[i] <= nums[i + 1]:
                err = True

        if not 3>= abs(nums[i] - nums[i + 1]) >= 1:
            err = True
        if err:
            if damepenr_used:
                break
            else:
                damepenr_used = True
                v0 = list(nums)
                v1 = list(nums)
                v2 = list(nums)

                v0.pop(i-1)
                v1.pop(i)
                v2.pop(i+1)

                return verify_nums(v1, None, True) or verify_nums(v2, None, True) or verify_nums(v0, None, True)                        
    else:
        return True
    return False





for line in file:
    nums = line.split()
    nums = [int(num) for num in nums]
    damepenr_used = False
    if nums[0] == nums[1]:
        nums.pop(0)
        damepenr_used = True

    if verify_nums(nums, None, damepenr_used):
        result += 1
    else:
        print(damepenr_used,nums)
    

print(result)