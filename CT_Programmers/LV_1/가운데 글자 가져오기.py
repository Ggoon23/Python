s="abcde"

def solution(s):
    l = len(s)
    if l%2==0:
        ll=l//2-1
        answer=s[ll:ll+2]
    else:
        ll=(l+1)//2-1
        answer=s[ll:ll+1]
    return "".join(answer)

print(solution(s))