def solution(a, d, included):
    s=[]
    i=0
    answer=0
    while i<len(included):
        s.append(a+i*d)
        i+=1
    for b in range(0,len(included)) :
        if included[b] :
            answer+=int(s[b])
        
    return answer