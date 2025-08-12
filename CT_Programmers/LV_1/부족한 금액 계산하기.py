price = 3
money = 20
count = 4

def solution(price, money, count):
    return ((count*(count+1))/2)*price-money if ((count*(count+1))/2)*price-money>=0 else 0

print(solution(price,money,count))