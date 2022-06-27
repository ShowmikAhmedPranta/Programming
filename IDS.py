graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : ['11','10'],
  '4' : ['8'],
  '8' : [],
  '10':['9','13'],
  '13':[],
  '9':[],
  '11':[]
}

visited=[]
stack=[]

start='5'
count=0
maxx=5
def DFS(graph,start,count):
    st=[]
    visited.append(start)
    stack.append(start)
    
    while(stack and len(stack)<count):
        m=stack.pop(-1)
        print(m)
        for neighbors in graph[m]:
            if(neighbors not in visited):
                visited.append(neighbors)
                stack.append(neighbors)
                

DFS(graph,start,3)


    