d = [1,3,2,5,4]
budget = 9

def solution(d, budget):
    cnt = 0
    for i in range(len(d)):
        budget = budget - min(d)
        d.remove(min(d))
        if budget >= 0 :
            cnt += 1
        else :
            break
    return cnt

print(solution(d, budget))