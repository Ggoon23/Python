keyinput = ["left", "right", "up", "right", "right"]
board = [11,11]

def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput :
        if i == "up" :
            answer[1] += 1
            if answer[1] > (board[1]-1)//2 :
                answer[1] -= 1
        elif i == "down" :
            answer[1] -= 1
            if answer[1] < (-1 * ((board[1]-1)//2)) :
                answer[1] += 1
        elif i == "right" : 
            answer[0] += 1
            if answer[0] >  (board[0]-1)//2 :
                answer[0] -= 1
        elif i == "left" :
            answer[0] -= 1
            if answer[0] < (-1 * ((board[0]-1)//2)) :
                answer[0] += 1
    return answer

print(solution(keyinput,board))