s = "10 Z 20 Z 1"

def solution(s):
    ss = s[:].split()
    answer = 0
    for i in ss :
        if i != "Z" :
            answer += int(i)
            Z = int(i)
        else :
            answer -= Z
    return answer

print(solution(s))