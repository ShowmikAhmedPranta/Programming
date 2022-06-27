visited=[]
queue=[]

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

costmap={}

def ucs(sn,gl,visited,queue):
    visited.append(sn)
    queue.append(sn)
    
    while queue:
        m=queue.pop(0)
        print(m)
        if(m==gl):
            return True
        
        for neighbours in graph[m]:
            if neighbours not in visited:
                if m in costmap.keys():
                    costmap[neighbours]=cost[(m,neighbours)]+costmap[m]
                else:
                    costmap[m]=0
                    costmap[neighbours]=cost[(m,neighbours)]
                visited.append(neighbours)
                queue.append(neighbours)
                
                queue1=[]
                for i in sorted(costmap.values()):
                    for j in costmap.keys():
                        if(costmap[j]==i and j in queue):
                            queue1.append(j)
                queue=queue1  
    return False

ucs(0,4,visited,queue)
print(visited)
print(costmap[4])
                