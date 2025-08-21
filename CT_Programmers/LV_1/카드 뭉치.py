def solution(cards1, cards2, goal):
    for i in goal:
        if i in cards1 and cards1[0] == i:
            cards1.pop(0)
        elif i in cards2 and cards2[0] == i:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))