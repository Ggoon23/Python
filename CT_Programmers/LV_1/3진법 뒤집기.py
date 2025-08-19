n=45

def solution(n):
    nn=''
    while n > 0 :
        nn += str(n % 3)
        n //= 3
    answer = int(nn,3)
    return answer

print(solution(n))