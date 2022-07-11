import sys

class Edge:
    def __init__(self):
        self.vertex1 = 0 
        self.vertex2 = 0 
        self.weight = 0 
        self.edge_deleted = 0
        
class Graph:
    def __init__(self):
        self.vertex = [0]*100
        self.edges = 0 

MAX_V = 100 #圖裡面最多會出現多少個點
TRUE = 1 
FALSE = 0 

E = [None] * MAX_V #放所有邊(Edge)，正常是MAX_V-1，但是因為第一格不會放會從[1]開始，所以用MAX_V就好
T = Graph()
total_vertex = 0
total_edge = 0
adjmatrix = [[0]*MAX_V for row in range (MAX_V)] #二為矩陣，把檔案的東西讀進來
 
def build_adjmatrix():
    global adjmatrix
    global total_vertex
    
    try:
        inputStream = open('kruskal.dat','r') #r是讀檔(read)，w是write
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    
    #讀檔案，把內容轉成數字，但是連特殊字元ex:換行符號都會讀到，所以用strip把他拿掉
    total_vertex = eval(inputStream.readline().strip('\n'))
    
    for vi in range(1, total_vertex+1):
        #.split(' ')用空格去做切割
        temp = [0] + inputStream.readline().strip('\n').split(' ')
        for vj in range(1, total_vertex+1):
            adjmatrix[vi][vj] = eval(temp[vj])
            
    #讀檔都要記得把檔案關掉以後才能開
    inputStream.close()
    
def adjust():
    global FALSE #先把所有邊都設成還沒刪除的
    global total_vertex
    global adjmatrix
    
    for i in range(1, total_vertex+1):
        for j in range(i+1, total_vertex+1):
            weight = adjmatrix[i][j]
            if weight!= 0:
                e = Edge()
                e.vertex1 = i        
                e.vertex2 = j        
                e.weight = weight
                e.edge_deleted = FALSE
                addEdge(e)
            
def addEdge(e):
    global E
    global total_edge
    
    total_edge += 1
    E[total_edge] = e
    
def showEdge():
    global E
    global total_vertex
    global total_edge
    
    i = 1
    print("Total vertex: ", total_vertex)
    print("Total edge: ", total_edge)
    print()
    
    while i <= total_edge:
        print('v%d <---> v%d,' %(E[i].vertex1, E[i].vertex2), end="")
        print(" weight: ", E[i].weight)
        i += 1
    
def kruskal():
    global T    
    global total_vertex
    
    loop = 1
    T.edges = 0
    
    print()
    while T.edges != total_vertex-1:
        e = mincostEdge()
        if cyclicT(e) != 1: #回傳的不是TRUE代表不是cyclic
            print("%d th min edge: " % loop, end='')
            loop += 1
            print("v%d <---> v%d," % (e.vertex1, e.vertex2), end="")
            print(" weight: ", e.weight)
            
           
def cyclicT(e):
    global TRUE
    global FALSE
    global T
    
    v1 = e.vertex1
    v2 = e.vertex2
    T.vertex[v1] += 1 
    T.vertex[v2] += 1
    T.edges += 1
    
    
    if T.vertex[v1] >= 2 and T.vertex[v2] >= 2:#形成cycle
        T.vertex[v1] -= 1
        T.vertex[v2] -= 1
        T.edges -= 1
        return TRUE 
    else:
        return FALSE 
           
def mincostEdge():
    global TRUE
    global FALSE
    global E
    global total_edge
    
    minE = 0
    minweight = 10000000
    
    for i in range(1, total_edge+1):
        if E[i].edge_deleted == FALSE and E[i].weight < minweight:
            minweight = E[i].weight
            minE = i
    
    E[minE].edge_deleted = TRUE
    return E[minE]
      

def main():
    build_adjmatrix()
    adjust()
    showEdge()
    kruskal()
    
main()
