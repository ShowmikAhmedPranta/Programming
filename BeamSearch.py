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
beam_len=4
def BeamSearch(graph,start, goal,beam_len):
    visited.append(start)
    queue.append(start)
    
    while queue:
        m=queue.pop(0)
        print(m)
        if(m==goal):
            print("Goal found")
            return 0
        
        for neighbours in graph[m]:
            if neighbours not in visited:
                visited.append(neighbours)
                queue.append(neighbours)
                queue.sort(key=lambda e:int(h[e]))
                while(len(queue)>beam_len):
                    queue.pop(-1)
                    
BeamSearch(graph,'S','G',4)
                    
                    
                
                
    