def solution(s, skip, index):
    result=''
    for i in s:
        count=0
        while count < index:
            i=chr(ord(i)+1)
            if i > 'z':
                i='a'
            if i not in skip :
                count +=1
        result+=i
    return result