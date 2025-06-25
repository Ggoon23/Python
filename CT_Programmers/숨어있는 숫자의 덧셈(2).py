my_string = "aAb1B2cC34oOp"

import re

def solution(my_string):
    numbers = re.findall(r'\d+', my_string)
    return sum(map(int, numbers))

print(solution(my_string))