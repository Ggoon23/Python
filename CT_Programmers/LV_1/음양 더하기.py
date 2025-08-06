absolutes=[4,7,12]
signs=[True,False,True]

def solution(absolutes, signs):
    return sum(absolutes[i]*(1 if signs[i]==True else -1)for i in range(len(absolutes)))

print(solution(absolutes,signs))