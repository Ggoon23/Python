s = "abcabcadc"

def solution(s):
    ss = s[:]
    answer = []
    for i in ss :
        count = 0
        for j in ss :
            if i == j:
                count += 1
        if count == 1 :
            answer.append(i)
    return "".join(sorted(answer))

print(solution(s))