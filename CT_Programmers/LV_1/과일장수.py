def solution(k, m, score):
    return m*sum(sorted(score,reverse=True)[m-1:m*len(score)//m:m])
k=3
m=4
score = [1, 2, 3, 1, 2, 3, 1]

print(solution(k,m,score))