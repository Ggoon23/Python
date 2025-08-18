s = "banana"

def solution(s):
    return [s[i::-1].find(s[i],1) for i in range(len(s))]


print(solution(s))