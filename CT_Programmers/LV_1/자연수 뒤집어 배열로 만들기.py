n = 12345

def solution(n):
    return [int(i) for i in (str(n))][::-1]

print(solution(n))