graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

def DLS(src,target,maxDepth):
    if(src == target):
        return True
    if(maxDepth <= 0):
        return False

    for i in graph[src]:
            if(DLS(i,target,maxDepth-1)):
                return True
    return False


def IDDFS(src, target, maxDepth):
    for i in range(maxDepth):
        if (DLS(src, target, i)):
            return True
    return False

target = '18'
maxDepth = 3
src = '5'

if(IDDFS(src, target, maxDepth) == True):
    print ("Target is reachable")
else:
    print ("Target is not reachable")

# This code is contributed by Neelam Pandey
