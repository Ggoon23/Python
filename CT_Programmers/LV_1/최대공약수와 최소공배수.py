n=3
m=12

import math
def solution(n, m):
    return [math.gcd(n,m), math.lcm(n,m)]

print(solution(n,m))