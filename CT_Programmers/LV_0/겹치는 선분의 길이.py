lines = [[0, 1], [2, 5], [3, 9]]

def solution(lines):
    arr = [0] * 201
    for s, e in lines:
        for i in range(s, e):
            arr[i + 100] += 1
    return sum(x > 1 for x in arr)

print(solution(lines))