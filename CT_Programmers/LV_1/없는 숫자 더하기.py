numbers=[1,2,3,4,6,7,8,0]

def solution(numbers):
    sum = 0
    for i in range(10):
        print(numbers)
        if i in numbers:
            numbers.remove(i)
        else :
            sum += i
    return sum

print(solution(numbers))