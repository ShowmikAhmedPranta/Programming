class STACKwithLINKEDLIST:
    def __init__(self):
        self._Data={}
        
    def PUSH(self, value, nxt):
        if(nxt==None or value==None):
            raise Exception("Pointing value is not given")
        else:
            self._value=value
            self._nxt = nxt
            self._Data[self._value]=self._nxt
            self._head=value
            if(len(self._Data)==0):
                self._tail= nxt
        
    def TOP(self):
        if(len(self._Data)==0):
            raise Exception("No head")
        else:
            print(self._head)
        
    def TRAVERSE(self):
        if(len(self._Data)==0):
            raise Exception("List is empty")
        j=self._head
        for i in range(len(self._Data)):
            print(j,"---->",self._Data[j])
            j=self._Data[j]
            
            
    def POp(self):
        if(len(self._Data)==0):
            raise Exception("Linked list is empty")
        elif(len(self._Data)==1):
            del self._Data[self._head]
            self._head=None
        else:
            b=self._head
            a=self._Data[self._head]
            del self._Data[self._head]
            self._head = a
            return b
    def IS_EMPTY(self):
        if(len(self._Data)==0):
            return True
        else:
            return False
        
