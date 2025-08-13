arr = [5,9,7,10]
divisor = 5

def solution(arr, divisor):
    answer=[]
    for i in arr:
        if i%divisor==0:
            answer.append(i)
    return sorted(answer) if answer !=[] else [-1]

print(solution(arr, divisor))