before = "allpe"
after = "apple"

def solution(before, after):
    a = list(after)
    b = list(before)
    for i in a :
        if i in b:
            b.remove(i)
    if b == []:
        return 1
    else :
        return 0

print(solution(before,after))