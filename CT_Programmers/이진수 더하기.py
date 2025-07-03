bin1 = "10"
bin2 = "11"


def solution(bin1, bin2):
    return format((int(bin1,2)+int(bin2,2)),"0b")

print(solution(bin1, bin2))