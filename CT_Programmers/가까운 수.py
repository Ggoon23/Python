array = [3,10,28,9,28,12]
n = 20

def solution(array, n):
    ss= [abs(n-i) for i in array]
    minnum_mi = min(ss)
    minnum = max(array)
    for i in range (len(ss)) :
        if ss[i] == minnum_mi :
            minnum
            if minnum > array[i] :
                minnum = array[i]
    return minnum

print(solution(array, n))