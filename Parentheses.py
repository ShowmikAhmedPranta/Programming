#checking parentheses using stack
#expression like [4+{3*(2+1)-5}]
#let's see how checking is done.
#stack is FILO or LIFO(last in first out)
class Parentheses:
    def __init__(self, expression):
        self.expression = expression
        self.left= ['(','{','[']
        self.right=[')','}',']']
        #constructor function created
        print(self.checking())
        
    def checking(self):
        stack_left=[]  #stack created.
        for i in self.expression:
            if i in self.left:
                stack_left.append(i)
            elif i in self.right:
                if(len(stack_left)<=0):
                    #right cannot exist without left
                    return False
                else:
                    temporary=stack_left.pop()
                    if(self.left.index(temporary)!=self.right.index(i)):
                        #i was in right
                        #temporary from stack_left via left
                        #( corresponds to )    .......
                        return False
                    #must return an empty stack. Otherwise not balanced.
        if(len(stack_left)==0):
            return True
        #so the program ran well.
        