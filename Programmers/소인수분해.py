
n = 12

def solution(n):
    answer = []
    for i in range(2,n) :
        while n/i == int(n/i) :
            n = n/i
            if i not in answer :
                answer.append(i)
    return answer

print(solution(n))