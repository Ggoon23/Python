food=[1,3,4,6]

def solution(food):
    s = []
    for i in range(1,len(food)):
        for j in range((food[i]//2)):
            s.append(f"{i}")
    return "".join(s+["0"]+s[::-1])

print(solution(food))