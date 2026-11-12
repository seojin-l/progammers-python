def solution(a, b):
    answer = 0
    t1=str(a)+str(b)
    t2=2*a*b
    if int(t1)>=t2:
        answer=t1
    else:
        answer=t2
    return int(answer)