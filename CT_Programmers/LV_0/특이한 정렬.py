numlist = [1, 2, 3, 4, 5, 6]
n= 4

def solution(numlist, n):
    numlist.sort(key=lambda x: (abs(x - n), -x))
    return numlist

print(solution(numlist, n))