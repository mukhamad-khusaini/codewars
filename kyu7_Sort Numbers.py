def solution(nums):
    if  nums: 
        nums.sort()
        return nums
    else: return []

print(solution(None))