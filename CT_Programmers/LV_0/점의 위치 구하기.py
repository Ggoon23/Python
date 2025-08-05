dot = [2,4]

def solution(dot):
    a,b = dot[0],dot[1]
    if a*b>0 :
        if a >0 :
            return 1
        else :
            return 3
    else :
        if a > 0 :
            return 4
        else :
            return 3

print(solution(dot))