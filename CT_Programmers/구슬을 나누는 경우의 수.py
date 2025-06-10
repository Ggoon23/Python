balls = 3
share = 2

def solution(balls, share):
    a , b = 1, 1
    for i in range (balls-share+1,balls+1):
        a *=i
    for i in range (1,share+1) :
        b *=i
    return int(a / b)

print(solution(balls,share))