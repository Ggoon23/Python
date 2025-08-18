s = "AB"
n = 1

def solution(s, n):
    answer=[]
    up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']*10
    dn = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x','y','z']*10
    ss=[i for i in s]
    for i in ss:
        if i==" ":
            answer.append(" ")
        elif i in up :
            answer.append(up[up.index(i)+n])
        elif i in dn :
            answer.append(dn[dn.index(i)+n])
    return "".join(answer)

print(solution(s,n))