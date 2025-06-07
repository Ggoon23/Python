emergency = [3,76,24]

def solution(emergency):
    answer = [0 for a in range (len(emergency))]
    for i in range(len(emergency)) :
        answer[emergency.index(max(emergency))] = i+1
        emergency[emergency.index(max(emergency))] = 0
    return answer
print(solution(emergency))