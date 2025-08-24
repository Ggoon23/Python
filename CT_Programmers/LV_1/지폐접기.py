def solution(wallet, bill):
    answer = 0
    while max(bill) > max(wallet):
        bill[bill.index(max(bill))] //= 2
        answer += 1
    while min(bill) > min(wallet):
        bill[bill.index(max(bill))] //= 2
        answer += 1
    return answer

wallet = [30,15]
bill = [26,17]

print(solution(wallet,bill))