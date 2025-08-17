sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    w = []
    h = []
    for size in sizes:
        w.append(max(size))
        h.append(min(size))
    return max(w) * max(h)

print(solution(sizes))