from STACK import STack

a=STack()

def reversal(A): #A is an array
    l=len(A)
    for i in A:
        a.PUSH(i)
    
    A=[]
    for i in range(l):
        A.append(a.POP())
    
    return A


        
    
        
    
        