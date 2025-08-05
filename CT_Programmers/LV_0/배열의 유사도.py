s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]

def solution(s1, s2):
    answer = 0
    for i in s1 :
        if i in s2 :
            answer +=1
    return answer

print(solution(s1,s2))