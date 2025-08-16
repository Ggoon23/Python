s="try hello world"

def solution(s):
    answer = []
    cnt = 0
    for ch in s:
        if ch == " ":
            answer.append(" ")
            cnt = 0
        else:
            if cnt % 2 == 0:
                answer.append(ch.upper())
            else:
                answer.append(ch.lower())
            cnt += 1
    return "".join(answer)

print(solution(s))