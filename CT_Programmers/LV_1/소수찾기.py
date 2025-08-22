
def solution(n):
    return sum(all(j%i for i in range(2,int(j**0.5)+1)) for j in range(2,n+1))

n = 10
print(solution(n))