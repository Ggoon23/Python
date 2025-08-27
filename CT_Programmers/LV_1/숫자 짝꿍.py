def solution(X, Y):
    count_x = [0] * 10
    count_y = [0] * 10
    
    for c in X:
        count_x[int(c)] += 1
    for c in Y:
        count_y[int(c)] += 1
    
    result = ""
    for i in range(9, -1, -1):
        cnt = min(count_x[i], count_y[i])
        result += str(i) * cnt
    
    return "-1" if not result else "0" if result[0] == "0" else result


X = "12321"
Y = "42531"

print(solution(X,Y))