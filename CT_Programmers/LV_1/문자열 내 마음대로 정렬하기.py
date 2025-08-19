strings = ["sun", "bed", "car"]
n=1

def solution(strings, n):
    s = sorted([i[n]+i for i in strings])
    return [i[1:] for i in s ]

print(solution(strings, n))