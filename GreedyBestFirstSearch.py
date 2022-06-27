graph={'S':['A','B','C'],
       'A':['D','E','G'],
       'B':[],
       'C':[],
       'D':[],
       'E':[],
       'G':[]}

h={'S':8,
   'A':3,
   'B':4,
   'C':8,
   'D':999,
   'E':999,
   'G':0}

visited=[]
queue=[]
def GreedyBFS(graph,start,goal):
    visited.append(start)
    queue.append(start)
    
    while queue:
        minim=1000
        m='Z'
        for i in queue:
            if(h[i]<minim):
                minim=h[i]
                m=i
        queue.remove(m)
        print(m)
        if(m=='G'):
            print("Goal Found")
            return True
                
        for neighbors in graph[m]:
            if neighbors not in visited:
                visited.append(neighbors)
                queue.append(neighbors)
                
GreedyBFS(graph,'S','G')
            
    