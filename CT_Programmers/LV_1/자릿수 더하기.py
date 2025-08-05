n = 987

def solution(n):
    answer = 0
    for i in range (9):
        answer += (n//(10**i))%10
    return answer

print (solution(n))