n=20

def solution(n):
    n_list = []
    answer = []
    for i in range (1,n+1):
        if n % i == 0 :
            j = n//i
            n_list.append((i,j))

    return len(n_list)

print(solution(n))

'''
def solution(n):
    n_list = []
    answer = []
    for i in range (1,n+1):
        if n % i == 0 :
            n_list.append(i)

    for i in n_list :
        for j in range (1,n+1):
            if i * j == n:
                answer.append((i,j))
    return len(answer)
'''


