def solution(code):
    ret = ''
    mode = 0
    for i in range(0,len(code)) :
        if code[i] != "1" and mode == 0:
            if i %2==0:
                ret+=code[i]
        elif code[i] == "1" and mode == 0:
            mode = 1
        elif code[i] != "1" and mode ==1 :
            if i %2 != 0:
                ret+=code[i]

        elif code[i]== "1" and mode ==1 :
            mode = 0 
    if ret !="":
        return ret
    else :
        return "EMPTY"