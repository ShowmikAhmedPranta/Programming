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

def UCS(goal, start):
    print("The optimal path is:", end=" ")
    mincost = []
    queue = []
    
    m=max(graph.keys())
    #print(m)

    draph=[[] for i in range(m+2)]
    for keys in graph:
        for j in graph[keys]:
            draph[keys].append(j)

    #print(draph)
    
    for i in range(0,len(goal)):
        mincost.append(99999)
    queue.append([0, start])
    visited = {}
    count = 0
    while (len(queue) > 0):
        queue = sorted(queue)
        p = queue[-1]
        if(p[-1] == goal):
            print(goal)
        else:
            print(p[-1], end="--->>")
        del queue[-1]
        p[0] *= -1
        if (p[1] in goal):
            index = goal.index(p[1])
            if (mincost[index] == 99999):
                count += 1
            if (mincost[index] > p[0]):
                mincost[index] = p[0]
            del queue[-1]
            queue = sorted(queue)
            if (count == len(goal)):
                return mincost
        if (p[1] not in visited):
            for i in range(len(draph[p[1]])):
                queue.append( [(p[0] + cost[(p[1], draph[p[1]][i])])* -1, draph[p[1]][i]])
        visited[p[1]] = 1
    return mincost

begin=0
goal = [6]
cost = UCS(goal, begin)

print("\nMinimum cost from", begin, "to", goal[0],"is:",cost[0])
