import re

def solution(dartResult):
    pattern = re.compile(r'(\d{1,2})([SDT])([*#]?)')
    scores = []
    for num, bonus, option in pattern.findall(dartResult):
        num = int(num)
        if bonus == 'S':
            score = num
        elif bonus == 'D':
            score = num ** 2
        elif bonus == 'T':
            score = num ** 3
        if option == '*':
            score *= 2
            if scores:
                scores[-1] *= 2
        elif option == '#':
            score *= -1
        scores.append(score)
    return sum(scores)

dartResult = "1S2D*10T"
print(solution(dartResult))  # 출력: 37