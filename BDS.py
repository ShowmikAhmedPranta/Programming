graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : ['5'],
  '4' : ['8'],
  '8' : []
}

graphr = {}

for i in graph:
    #print(graph[i])
    for j in graph[i]:
        if(j not in graphr):
            graphr[j]=[]
            graphr[j].append(i)
        else:
            graphr[j].append(i)

visited = [] # List for visited nodes.
stack = []     #Initialize a queue
target=[3]
def dfs(visited, graph, node): #function for BFS
  visited.append(node)
  stack.append(node)

  while stack:          # Creating loop to visit each node
    m = stack.pop(-1) 
    print (m, end = " ")
    if(m in target):
        return 0

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        stack.append(neighbour)
        if(neighbour in target):
            return 0

# Driver Code
print("Following is the Depthth-First Search")
dfs(visited, graph, '5')    # function calling
print("\n")
visitedr = [] # List for visited nodes.
stackr = []     #Initialize a queue

def dfsr(visitedr, graphr, node): #function for BFS
  global target
  visitedr.append(node)
  stackr.append(node)

  while stackr:          # Creating loop to visit each node
    m = stackr.pop(-1) 
    print (m, end = " ")
    if(m in target):
        return 0

    for neighbour in graphr[m]:
      if neighbour not in visitedr:
        visitedr.append(neighbour)
        stackr.append(neighbour)
        if(neighbour in target):
            return 0

# Driver Code

print("Following is the Reversed Depthth-First Search")
dfsr(visitedr, graphr, '8')    # function calling
