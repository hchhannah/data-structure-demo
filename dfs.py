import sys

class Node:
    def __init__(self):
        self.vertex = 0
        self.link = None
       
MAX_V = 100
node = Node()
lastnode = Node()
adjlist = [None] * (MAX_V+1)
visited = [None] * (MAX_V+1)
total_vertex = 0

def build_adjlist():
    global node
    global lastnode
    global adjlist
    global visited
    global total_vertex
    
    try:
        inputStream = open('dfs.dat', 'r')
    except FileNotFoundError:
        print ("File not found")
        sys.exit(0)
        
    total_vertex = eval(inputStream.readline().strip('\n'))
    
    for vi in range (1, total_vertex+1):
        adjlist[vi] = Node()
        adjlist[vi].vertex = vi
        adjlist[vi].link = None
        visited[vi] = False
        
    weight = 0
        
    for vi in range (1, total_vertex+1):
        temp = [0] + inputStream.readline().strip().split(' ')
        for vj in range (1, total_vertex+1):
            weight = eval(temp[vj])
            if weight != 0:
                node = Node()
                node.vertex = vj
                node.link = None
                lastnode = searchlast(adjlist[vi])
                lastnode.link = node
    inputStream.close()
    
def searchlast(linklist):
    ptr = linklist
    while ptr.link != None:
        ptr = ptr.link
    return ptr
    
def show_adjlist():
    global adjlist
    
    for i in range(1, total_vertex+1):
        print("v%d" %adjlist[i].vertex, end="")
        ptr = adjlist[i].link
        while ptr != None:
            print("-->v%d" %ptr.vertex, end="")
            ptr = ptr.link
        print()
        
def dfs(v):
    global adjlist
    global visited
    
    print("v%d" %adjlist[v].vertex, end="")
    visited[v] = True
    ptr = adjlist[v].link
    
    while True:
        w = ptr.vertex
        if visited[w] != True:
            dfs(w)
        else:
            ptr = ptr.link
        
        if ptr == None:
            break
def main():
    build_adjlist()
    show_adjlist()
    dfs(1)
 
main()