def solution(name, yearning, photo):
    answer = []
    for i in photo:
        cnt = 0
        for j in range(len(name)):
            if name[j] in i:
                cnt += yearning[j]
        answer.append(cnt)
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5,10,1,3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning,photo))