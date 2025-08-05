sides = [11,7]

def solution(sides):
    return (sides[0]+sides[1]) - abs(sides[0]-sides[1])-1

print(solution(sides))