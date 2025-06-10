rsp = 205


def solution(rsp):
    answer = []
    rsp_list=list(str(rsp))
    for i in range (len(rsp_list)):
        if rsp_list[i] == '2':
            answer.append(0)
        elif rsp_list[i] == '0':
            answer.append(5)
        elif rsp_list[i] == '5':
            answer.append(2)
    return "".join(map(str,answer))

print(solution(rsp))