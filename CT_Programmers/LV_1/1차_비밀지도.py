def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        line = bin(a | b)[2:].zfill(n)
        answer.append(line.replace('1', '#').replace('0', ' '))
    return answer

n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]

print(solution(n,arr1,arr2))