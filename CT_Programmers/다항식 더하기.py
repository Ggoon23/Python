def solution(p):
    x, c = 0, 0
    for t in p.split(" + "):
        x += int(t[:-1]) if "x" in t and t != "x" else t == "x"
        c += int(t) if "x" not in t else 0
    return (f"{x}x" if x > 1 else "x" if x == 1 else "") + (" + " if x and c else "") + (str(c) if c else "")

print(solution("3x + 7 + x"))