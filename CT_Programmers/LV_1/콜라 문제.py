a=2
b=1
n=20

def solution(a, b, n):
    answer = 0
    while n//a != 0:
        cnt= (n//a)*b
        answer += (n//a)*b
        n=n%a+cnt
    return answer

print(solution(a,b,n))