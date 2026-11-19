def solution(cards1, cards2, goal):
    key1=0
    key2=0
    for i in range(0,len(goal)):
        if key1 < len(cards1) and goal[i] == cards1[key1]:
            key1+=1
        elif key2 < len(cards2) and goal[i] ==cards2[key2]:
            key2+=1
        else :
            return "No"
    answer = "Yes"
    return answer