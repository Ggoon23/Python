dots = [[-1, -1], [1, 1], [1, -1], [-1, 1]]

def solution(dots):
    answer = 0
    for i in range(4) :
        for j in range (4) :
         if dots[i][0] != dots[j][0] :
            if dots[i][1] != dots[j][1] :
                answer = abs(dots[i][0] - dots[j][0]) * abs( dots[i][1] - dots[j][1]) 
    return answer

print(solution(dots))