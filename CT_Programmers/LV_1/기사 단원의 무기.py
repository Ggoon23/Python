def cnt(k):
    s=0
    for i in range(1,int(k**(0.5))+1):
        if k%i==0:
            s += 2
    if k**(0.5)==int(k**(0.5)):
        s -= 1
    return s

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        s = cnt(i)
        if s>limit :
            s=power
        answer += s
    return answer

number = 5
limit = 3
power = 2

print(solution(number, limit, power))