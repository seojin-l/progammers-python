def solution(a, b):
    answer = 0
    t1=str(a)+str(b)
    t2=str(b)+str(a)
    if int(t1)>=int(t2):
        answer=t1
    else:
        answer=t2
    return int(answer)