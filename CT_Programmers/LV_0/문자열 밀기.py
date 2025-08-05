A = "hello"
B = "ohell"

def solution(A, B):
    answer = 0
    a = list(A)
    b = list(B)
    for i in range(len(A)):
        if a == b :
            break
        answer += 1
        a.insert(0,a.pop())
    return answer if answer != len(A) else -1
    

print(solution(A,B))