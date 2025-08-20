def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1 = cnt2 = cnt3 = 0
    for i, ans in enumerate(answers):
        if s1[i % len(s1)] == ans:
            cnt1 += 1
        if s2[i % len(s2)] == ans:
            cnt2 += 1
        if s3[i % len(s3)] == ans:
            cnt3 += 1
    max_cnt = max(cnt1, cnt2, cnt3)
    answer = []
    if cnt1 == max_cnt:
        answer.append(1)
    if cnt2 == max_cnt:
        answer.append(2)
    if cnt3 == max_cnt:
        answer.append(3)
    return answer

answers = [1,2,3,4,5]

print(solution(answers))