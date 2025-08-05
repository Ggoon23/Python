a = 7
b = 20

import math

def solution(a, b):
    c = math.gcd(a, b)
    bb = b // c

    while bb % 2 == 0:
        bb //= 2
    while bb % 5 == 0:
        bb //= 5

    if bb == 1:
        return 1
    else:
        return 2

print(solution(a,b))