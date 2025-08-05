my_string = "I love you"
num1 = 3
num2 = 6


def solution(my_string, num1, num2):
    ss = [a for a in my_string[:]]
    ss[num1], ss[num2] = ss[num2], ss[num1]
    return "".join(ss)

print(solution(my_string, num1, num2))