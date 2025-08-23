def solution(s, skip, index):
    ls = ''.join(chr(i) for i in range(97,123) if chr(i) not in skip)
    return ''.join(ls[(ls.index(c)+index)%len(ls)] for c in s)

s = "aukks"
skip = "wbqd"
index = 5

print(solution(s,skip,index))