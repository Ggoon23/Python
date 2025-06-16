quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]

def solution(quiz):
    answer = []
    for q in quiz :
        if int(q) == True :
            answer.append("O")
        else :
            answer.append("X")
    return answer
print(solution(quiz))