def solution(babbling):
    bb = ["aya", "ye", "woo", "ma"]
    bbb = ["ayaaya", "yeye", "woowoo", "mama"]
    answer = 0
    for i in babbling:
        if any(rep in i for rep in bbb):
            continue
        temp = i
        for j in bb:
            temp = temp.replace(j, " ")
        if temp.strip() == "":
            answer += 1
    return answer

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

print(solution(babbling))