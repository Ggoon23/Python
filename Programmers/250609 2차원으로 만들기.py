num_list = [1,2,3,4,5,6,7,8]
n=2

def solution(num_list, n):
    answer = [[0 for _ in range (n)] for a in range (int(len(num_list)/n))]
    for i in range (int(len(num_list)/n)):
        for j in range (n) :
            answer[i][j] = num_list[n*i+j]
    return answer

print(solution(num_list,n))