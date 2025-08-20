import datetime

def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    weekday = datetime.date(2016, a, b).weekday()
    return days[weekday]

a= 5
b= 24

print(solution(a,b))