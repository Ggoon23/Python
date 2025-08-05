spell = ["z", "d", "x"]
dic = ["def", "dww", "dzx", "loveaw"]


def solution(spell, dic):
    answer = 2
    for i in dic :
        count = 0
        for j in spell:
            if i.count(j) > 0 :
                count += 1
        if count == len(spell) :
            answer = 1
    return answer

print(solution(spell,dic))