my_string = "34 + 554"

'''
def solution(my_string):
    if '+' in my_string :
        answer = int(my_string[:my_string.index('+')-1]) + int(my_string[my_string.index('+')+2:])
    elif '-' in my_string :
        answer = int(my_string[:my_string.index('-')-1]) + int(my_string[my_string.index('-')+2:])
    return answer
'''

def solution(my_string):
    return eval(my_string)

print(solution(my_string))