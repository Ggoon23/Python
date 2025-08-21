def solution(nums):
    return len(list(set(nums))) if len(list(set(nums))) <= int(len(nums)/2) else int(len(nums)/2)

nums = [3,1,2,3]

print(solution(nums))