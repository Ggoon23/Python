numbers = [1,2,3]
direction = "right"

from collections import deque

def solution(numbers, direction):
    queue = deque(numbers)
    if direction == "right" :
        queue.appendleft(queue.pop())
    else :
        queue.append(queue.popleft())
    return list(queue)


print(solution(numbers,direction))


# queue.rotate(1) or queue.rotate(-1) 사용하면됨