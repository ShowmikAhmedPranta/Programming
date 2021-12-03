from STACK import STack
a = STack()

def Parentheses_Matching(A):
    left_parentheses = '[{('
    right_parentheses = ']})'
    
    for i in A:
        if i in left_parentheses:
            a.PUSH(i)
        if i in right_parentheses:
            if(a.IS_EMPTY()):
                return False
            else:
                if(right_parentheses.index(i) != left_parentheses.index(a.POP())):
                    return False
    return True