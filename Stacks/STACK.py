#Making a stack

class STack:
    def __init__(self):
        self._DAta = []
        
    def PUSH(self,e):
        self._DAta.append(e)
        
    def POP(self):
        if(len(self._DAta)==0):
            raise Exception('Stack is empty')
        else:
            return self._DAta.pop()
            
    def TOP(self):
        if(len(self._DAta)==0):
            raise Exception('Stack is empty')
        else:
            return self._DAta[-1]
        
    def LENGTH(self):
        return len(self._DAta)
    
    def IS_EMPTY(self):
        if(self.LENGTH==0):
            return True
        else:
            return False