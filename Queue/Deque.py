class DEQue:
    def __init__(self):
        self._Data = []
    
    def LENGTH(self):
        return len(self._Data)
    
    def add_first(self, value):
        self._Data.insert(0, value)
        
    def add_last(self, value):
        self._Data.append(value)
        
    def delete_first(self):
        if(self.LENGTH == 0):
            raise Exception("Queue is empty")
        else:
            a=self._Data[0]
            del self._Data[0]
            return a
            
    def delete_last(self):
        if(self.LENGTH == 0):
            raise Exception("Queue is empty")
        else:
            a=self._Data[-1]
            del self._Data[-1]
            return a
        
    def first(self):
        if(self.LENGTH == 0):
            raise Exception("Queue is empty")
        else:
            return self._Data[0]
        
    def last(self):
        if(self.LENGTH == 0):
            raise Exception("Queue is empty")
        else:
            return self._Data[-1]
        
            
    
        