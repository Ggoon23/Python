n = 10

def solution(n):
    if n%2==1:
        return 2
    else :
        for i in range (1,n):
            if n%i==1 :
                return i

print(solution(n))