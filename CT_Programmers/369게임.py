order = 29423

def solution(order):
    return  str(order).count('3')+str(order).count('6')+str(order).count('9')

print(solution(order))