my_string = "p2o4i8gj2"



def solution(my_string):
    return sorted([int(a) for a in my_string if a.isdigit() ])

print(solution(my_string))