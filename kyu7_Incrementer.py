def incrementer(nums):
    return [int(str(nums[i-1]+i)[-1]) for i in range(1, len(nums)+1)]