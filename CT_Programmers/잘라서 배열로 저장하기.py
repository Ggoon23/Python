my_str = "abc1Addfggg4556b"
n=6

def solution(my_str, n):
    answer = []
    if len(my_str)%n == 0 :
        a = len(my_str)//n
    else :
        a = len(my_str)//n+1
    for i in range (a) :
        answer.append(my_str[i*n:i*n+n])
    return answer

print(solution(my_str, n))