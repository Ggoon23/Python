k=3
score=[10, 100, 20, 150, 1, 100, 200]

def solution(k, score):
    answer = []
    s = []
    for i in score:
        s.append(i)
        if len(s) > k:
            s.remove(min(s))
        answer.append(min(s))
    return answer

print(solution(k,score))