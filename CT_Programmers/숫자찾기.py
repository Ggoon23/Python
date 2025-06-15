num = 29183
k =1

def solution(num, k):
    return int(str(num).find(str(k)))+1 if str(k) in str(num) else -1

print(solution(num,k))