s = "a234"

def solution(s):
    return len(s) in [4,6] and s.isnumeric()

print(solution(s))