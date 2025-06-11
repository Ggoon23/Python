cipher = "dfjardstddetckdaccccdegk"	
code = 4

def solution(cipher, code):
    return cipher[code-1::code]

print(solution(cipher,code))