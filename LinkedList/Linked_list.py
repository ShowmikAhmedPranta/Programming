class LINKEDLIST:
    def __init__(self):
        self._Data={}
        
    def FRONTNODE(self, value, nxt):
        if(nxt==None or value==None):
            raise Exception("Pointing value is not given")
        else:
            self._value=value
            self._nxt = nxt
            self._Data[self._value]=self._nxt
            self._head=value
            if(len(self._Data)==0):
                self._tail= nxt
        
    def HEAD(self):
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
            
    def MIDDLENODE(self, value, nxt): #deleting a middle node
        if((len(self._Data.keys())<2)):
            raise Exception("Front node or backnode is missing")
        else:
            temp = self._Data[value]
            self._Data[value]=nxt
            self._Data[nxt]=temp
            
    def DELETEFRONT(self):
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
        

            

            
            
        
           
            
            
          
#x=LINKEDLIST()
#x.FRONTNODE(15,10)
#x.FRONTNODE(10,15)
#x.TRAVERSE()
#x.HEAD()
#x.MIDDLENODE(20,18)
#x.TRAVERSE()


            
            
            
        
        
    
        
        