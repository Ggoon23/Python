my_string = "aAb1B2cC34oOp"

def solution(my_string):
    answer = 0
    list_my = [a for a in my_string[:]]
    for i in list_my :
        if i in ['0','1','2','3','4','5','6','7','8','9'] :
            answer += int(i)
    return answer

print(solution(my_string))