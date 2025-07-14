i = 1
j = 13
k = 1

def solution(i, j, k):
    answer = 0
    for d in range(i, j+1):
        if str(k) in str(d) :
            answer += str(d).count(str(k))
    return answer

print(solution(i,j,k))
