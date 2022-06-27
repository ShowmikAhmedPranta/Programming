graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
stack = []     #Initialize a queue

def dfs(visited, graph, node): #function for BFS
  visited.append(node)
  stack.append(node)

  while stack:          # Creating loop to visit each node
    m = stack.pop(-1) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        stack.append(neighbour)

# Driver Code
print("Following is the Depthth-First Search")
dfs(visited, graph, '5')    # function calling
