graph={
    0:[1,3],
    1:[6],
    2:[1],
    3:[1,6,4],
    4:[2,5],
    5:[2,6],
    6:[4]
    }

cost={(0, 1): 2,
 (0, 3): 5,
 (1, 6): 1,
 (3, 1): 5,
 (3, 6): 6,
 (3, 4): 2,
 (2, 1): 4,
 (4, 2): 4,
 (4, 5): 3,
 (5, 2): 6,
 (5, 6): 3,
 (6, 4): 7}

h={0:8,
   1:8,
   2:4,
   3:3,
   4:999,
   5:999,
   6:999
   }

cost_map={}

queue=[]
visited=[]

def A_star(graph,start,goal):
    queue.append(start)
    visited.append(start)
    cost_map[start]=h[start]
    
    while queue:
        m=queue.pop(0)
        print(m)
        
        for neighbours in graph[m]:
            if neighbours not in visited:
                cost_map[neighbours]=cost[(m,neighbours)]+cost_map[m]+h[neighbours]
                queue.append(neighbours)
                visited.append(neighbours)
                queue.sort(key=lambda k:cost_map[k])
            
A_star(graph,0,6)
            
                
        
    