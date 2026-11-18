def solution(s):
    count=0
    while len(s)>=1:
        x=s[0]
        x_count=0
        nx_count=0
        for i in range(0,len(s)):
            if s[i] == x:
                x_count+=1
            else :
                nx_count+=1
            if x_count ==nx_count :
                break
        count+=1
        s=s[i+1:]
    return count