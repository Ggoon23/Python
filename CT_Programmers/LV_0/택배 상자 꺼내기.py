n=22
w=6
num=8

import math
def solution(n, w, num):
    if not (1 <= num <= n) or w <= 0:
        return 0

    num_floor_idx = (num - 1) // w
    num_pos_in_floor = (num - 1) % w

    actual_col_idx = num_pos_in_floor if num_floor_idx % 2 == 0 else (w - 1 - num_pos_in_floor)

    count = 1 
    total_floors = math.ceil(n / w)
    
    for current_floor_idx in range(num_floor_idx + 1, total_floors):
        floor_start_box_num = current_floor_idx * w + 1
        
        if current_floor_idx % 2 == 0:
            box_in_column = floor_start_box_num + actual_col_idx
        else:
            box_in_column = floor_start_box_num + (w - 1 - actual_col_idx)
        
        if box_in_column <= n:
            count += 1
        else:
            break

    return count

print(solution(n,w,num))