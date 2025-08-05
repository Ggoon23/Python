my_string = "We are the world"

def solution(my_string):
    strlist = [a for a in my_string[:]]
    answer = []
    for i in (strlist) :
        if i not in answer :
            answer.append(i)
    return "".join(answer)

print(solution(my_string))