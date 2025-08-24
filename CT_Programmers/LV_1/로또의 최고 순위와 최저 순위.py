def solution(lottos, win_nums):
    answer = [7,7]
    for i in lottos:
        if i in win_nums:
            answer[0] -= 1
            answer[1] -= 1
        elif i == 0:
            answer[0] -= 1
    return [i if i!= 7 else 6 for i in answer ]

lottos = [0,0,0,0,0,0]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos,win_nums))