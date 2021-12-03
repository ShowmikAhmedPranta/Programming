# HTML tag matching

from STACK import STack

def HTML_Tag(A):
    a= STack()
    i = A.find('<')
    while(i != -1):
        j=A.find('>',i+1)
        if(j==-1):
            return False 
        tag = A[i+1:j]
        if(not tag.startswith('/')):
            a.PUSH(tag)
        else:
            if(a.LENGTH()==0):
                return False
            else:
                if(tag[1:] != a.POP()):
                    return False
        i = A.find('<',j+1)
    return a.LENGTH()==0