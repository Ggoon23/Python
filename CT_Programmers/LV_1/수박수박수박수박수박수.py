n=3

def solution(n):
    answer=[]
    a = 0
    while a!=n:
        if a%2==0:
            answer.append("수")
        else :
            answer.append("박")
        a += 1
    return "".join(answer)


print(solution(n))