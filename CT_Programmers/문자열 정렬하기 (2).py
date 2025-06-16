my_string = "heLLo"

def solution(my_string):
    return "".join(sorted(my_string.lower()))

print(solution(my_string))