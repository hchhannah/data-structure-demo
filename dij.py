import sys

MAX_V = 100
Visited = 1
Not_visited = 0
Infinite = 1073741823

#習慣從1開始所以MAX_V+1個
A = [[0] * (MAX_V+1) for row in range(MAX_V+1)] 
D = [0] * (MAX_V+1) #D=Distance
S = [0] * (MAX_V+1) #記錄他有沒有被拜訪過
P = [0] * (MAX_V+1) #path路徑

source = 0 #從哪裡來
sink = 0 #走到哪裡
N = 0 #實際上有多少個點
top = -1
step = 1

Stack = [0] * (MAX_V+1)

def init():
    global A
    global D
    global S
    global P
    global Infinte
    global N
    global Visited
    global Not_visited
    global source
    global sink
    
    weight = 0 
    done = False
    
    try:
        inputStream = open('sh_path.dat','r')
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
        
    try:
        N = eval(inputStream.readline().strip('\n'))
    except Exception:
        pass
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            A[i][j] = Infinite
    
    while done == False:
        try:
            temp = inputStream.readline().strip('\n').split(' ')
            i = eval(temp[0])
            j = eval(temp[1])
            weight = eval(temp[2])
        except Exception:
            done = True
            
        A[i][j] = weight
        
    inputStream.close()       
    
    source = eval(input("Enter a source node: "))
    sink = eval(input("Enter a sink node: "))
    
    for i in range(1, N+1):
        S[i] = Not_visited
        D[i] = A[source][i]
        P[i] = source
    S[source] = Visited
    D[source] = 0
    
    output_step()
    
def output_step():
    global D
    global P
    global N
    global Infinite
    print()
    print("Step: ", step)
    print()
    print("D: ")
    
    for i in range(1, N+1):
        if D[i] == Infinite:
            print("-----", end="")
        else:
            print("%5d" %D[i], end="")
    print()
    
    print("P: ")
    for i in range(1, N+1):
        print("%5d" %P[i], end="")
    print()

def access():
    global step
    global A
    global D
    global S
    global P
    global N
    global Not_visited
    global Visited
    
    for step in range(2, N+1):
        t = minD()
        S[t] = Visited
        for i in range(1, N+1):
            if S[i] == Not_visited and D[t]+A[t][i] < D[i]:
                D[i] = D[t]+A[t][i] #取代
                P[i] = t
        output_step()

def minD():
    global Infinite
    global S
    global Not_visited
    global N

    t = 0
    minimum = Infinite 
    
    for i  in range(1, N+1):
        if S[i] == Not_visited and D[i] < minimum:
            minimum = D[i]
            t = i
    return t

def output_path():
    global Infinte
    global A
    global D
    global P
    global source
    global sink
    
    node = sink
    
    if sink == source or D[sink] == Infinite:
        print("\nNode %d has no path to Node %d" % (source), end ="")
        return
    
    print("\n")
    print("The shortest path from V%d to V%d: " %(source, sink),end ="")
    print()
    print("v%d" % source, end="")
    while node != source:
        Push(node)
        node = P[node]
    while node != sink:
        node = Pop()
        print("--%d--> " %A[P[node]][node],end="")
        print("v%d" % node, end="")
    print()
    print("\nTotal length: %d" % D[sink])

def Push(value):
    global MAX_V
    global top
    global Stack
    
    if top >= MAX_V:
        print("Stack overflow!")
        sys.exit(1)
    else:
        top += 1
        Stack[top] = value
        
def Pop():
    global top
    global Stack
    
    if top < 0:
        print("Stack is empty!")
        sys.exit(1)
    temp = Stack[top]
    top -= 1
    return temp
  

def main():
    init()
    output_step()
    access()  
    output_path()
    
main()
