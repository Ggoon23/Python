
numbers = [1, 2, -3, 4, -5]

def solution(numbers):
    numbers.sort()
    a = numbers[0]*numbers[1]
    b = numbers[-1]*numbers[-2]
    return max(a,b)


print(solution(numbers))