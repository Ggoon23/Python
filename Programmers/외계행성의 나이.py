age = 23

def solution(age):
    age_type=['a','b','c','d','e','f','g','h','i','j']
    answer=["" for i in range(4)]
    for i in range (1,5) :
        a = 10**(4-i)
        if age >= a :
            answer[i-1]=age_type[age // a]
            age -= (age//a)*a
        elif age == 0 :
            answer[i-1] = age_type[age]
        else :
            continue
    return "".join(answer)
print(solution(age))

'''
 "".join(age)으로 answer의 요소들을 연결하여 출력할 수 있음
 문자열이 아닌경우 map(str,age)를 활용해 문자열로 변경해 출력가능
 join을 사용하지 않는 경우는 아래를 활용해야함
 for char in my_array:
    result_string += char
'''
