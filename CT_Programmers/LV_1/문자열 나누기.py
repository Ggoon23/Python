def solution(s):
    cnt = 0
    answer = 0
    for i in range(len(s)):
        if cnt <= i:
            fst = s[i]
            a = 0
            b = 0
            for j in range(i,len(s)):
                if s[j] == fst:
                    a += 1
                    cnt += 1
                else :
                    b += 1
                    cnt += 1
                if a == b:
                    answer += 1
                    break
    if cnt != i:
        answer += 1
    return answer


s="abracadabra"

print(solution(s))