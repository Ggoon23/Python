quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]

def solution(quiz):
    return ["O" if eval(q.split('=')[0]) == int(q.split('=')[1]) else "X" for q in quiz]

print(solution(quiz))