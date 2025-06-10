n = 3628800

import math
def solution(n):
    for i in range (1,12) :
        if math.factorial(i) > n:
            break
    return i-1

print(solution(n))
print(solution(7))