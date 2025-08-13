t="3141592"
p="3"

def solution(t, p):
    s = [i for i in t]
    ss = ["" for i in range(len(t)-len(p)+1)]
    count = 0
    for j in range(len(p)):
        for i in range(len(t)-len(p)+1):
            ss[i] += s[i+j]
    for i in ss:
        if int(i)<= int(p):
            count += 1
    return count

print(solution(t,p))