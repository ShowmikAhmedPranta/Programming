class QUeue:
    def __init__(self):
        self._DAta=[]
        
    def ENQUEUE(self,e):
        self._DAta.append(e)
        
    def DEQUEUE(self,e):
        if(a.IS_EMPTY):
            raise Exception("Queue is empty")
        else:
            a=self._DAta[0]
            del self._DAta[0]
            return a
        
    def IS_EMPTY(self):
        return len(self._DAta)==0
    
    def LENGTH(self):
        return len(self._DAta)
    
    def FIRST(self):
        if(a.IS_EMPTY):
            raise Exception("Queue is empty")
        else:
            return self._DAta[0]
    
    
    