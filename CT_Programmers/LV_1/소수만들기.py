import itertools
def solution(nums):
    answer = 0
    for i in itertools.combinations(nums,3):
        cnt = 0
        for j in range(1,int(sum(i)+1)):
            if sum(i)%j == 0:
                cnt+=1
        if cnt == 2:
            answer += 1
    return answer

nums = [1,2,3,4]

print(solution(nums))