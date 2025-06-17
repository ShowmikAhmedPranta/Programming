import heapq

def tree(V, E, edges):
    trav=[]
    adj = [[] for _ in range(V)]
    for i in range(E):
        u, v, wt = edges[i]
        adj[u].append((v, wt))
        adj[v].append((u, wt))
        
    #create a priority queue
    pq = []
    
    visited = [False] * V
    res = 0
    
    #start with vertex 0
    
    heapq.heappush(pq,(0,0,0)) # weight, destination, source
    
    
    #Prim's algorithm
    
    while pq:
        wt, u, v = heapq.heappop(pq)
        if visited[u]:
            continue
        trav.append((wt, u, v))
        res += wt
        visited[u] = True
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v, u))
                
    return (res, trav)


if __name__ == "__main__":
    graph = [[0, 1, 5],
             [1, 2, 3],
             [0, 2, 1]]
    # Function call
    cost, path=tree(3, 3, graph)
    print(cost)
    for p in path:
        print("Source:",p[2],"destination:",p[1],"weight:",p[0])