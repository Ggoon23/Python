spell = ["p", "o", "s"]
dic = ["sod", "eocd", "qixm", "adio", "soo"]

def solution(spell, dic):
    answer = 0
    for i in dic :
        count = 0
        for j in spell :
            if j in i :
                count += 1
        if count == len(i) :
            answer += 1
    return answer

print(solution(spell,dic))