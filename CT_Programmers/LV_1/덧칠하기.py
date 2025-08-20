def solution(n, m, section):
    cnt = 0
    last = 0
    for s in section:
        if s > last:
            cnt += 1
            last = s + m - 1
    return cnt

n=8
m=4
section = [2,3,6]

print(solution(n,m,section))