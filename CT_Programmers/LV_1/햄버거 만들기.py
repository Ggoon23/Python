def solution(ingredient):
    cnt=0
    temp =[]
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1,2,3,1]:
            cnt += 1
            del temp[-4:]
    return cnt


ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

print(solution(ingredient))