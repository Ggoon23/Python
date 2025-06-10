box = [10,8,6]
n = 3


def solution(box, n):
    return (box[0]//n)*(box[1]//n)*box[2]//n

print(solution(box,n))