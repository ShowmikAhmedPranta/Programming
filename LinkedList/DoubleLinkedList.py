class doubleLinkedList:
    def __init__(self):
        self._a={}
        self._head=None
        
    def Push(self, val, pre, nex):
        self._a[val]={'pre':pre, 'nex':nex}
        self._head=val
        
    def Show(self):
        return self._a
    
    def Top(self):
        return self._head
    
    def Pop(self):
        if(len(self._a)==0):
            raise Exception("LinkedList is empty")
        cur_head=self._head
        cur_head_node=self._a[cur_head]
        self._head=self._a[cur_head]['pre']
        del self._a[cur_head]
        return [cur_head,cur_head_node]
    
"""
A=doubleLinkedList()
A.Push(10, 9, 11)
A.Push(11,10,12)
print(A.Show())
print(A.Top())
print(A.Pop())
print(A.Show())
print(A.Top())
print(A.Pop())
print(A.Show())
"""