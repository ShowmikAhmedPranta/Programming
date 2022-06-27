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
queue=[]
def HillClimbing(graph,node):
    visited.append(node)
    m=node
    while(graph[m]):
        temp=[]
        for i in graph[m]:
            temp.append(int(i))
        m=max(temp)
        print(m)
        HillClimbing(graph,str(m))

print(5)
HillClimbing(graph,'5')
print(visited)
        
    