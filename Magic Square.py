Max = 15
Square = [[0] * Max for row in range(Max)]
N = 0

def init():
    global N
    
    while True:
        N = int(input("\nEnter odd matrix size: "))
        if N % 2 == 0 or N <= 0 or N > 15:
            print("Should be > 0 and < 15 odd number", end = " ")
        else: 
            break
        
def Magic():
    global Square
    global N
    
    Square[0][(N-1)//2] = 1
    key = 2
    i = 0 
    j = (N-1)//2
    
    while key <= N*N:
        p = (i-1) % N 
        q = (j-1) % N
        if p<0:
            p = N-1
        if q<0:
            q = N-1
        if Square[p][q] != 0:
            i = (i+1) % N #向正下方移動 
        else: 
            i = p
            j = q
        Square[i][j] = key
        key += 1
 
def output():
    print("\nThe %d*%d Magic Matrix"%(N,N))
    print("-------------------------------")
    for i in range(N):
        for j in range(N):
            print("%-4d" % Square[i][j], end = " ")
        print()    

def main():
    init()
    Magic()
    output()
main()