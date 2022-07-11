N = 5
C = [[0]*N for row in range(N)]

def access_matrix(A, B):
    global C
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(N):
                sum += A[i][k] * B[k][j]
            C[i][j] = sum

def output_result(A, B):
    global C
    
    print("\nContent of Matrix A :\n")
    output_Matrix(A)
    print("\nContent of Matrix B :\n")
    output_Matrix(B)
    print("\nContent of Matrix C :\n")
    output_Matrix(C)
            
def output_Matrix(m):
    for i in range(N):
        for j in range(N):
            print(" ", m[i][j], end = ' ')
        print()
        
def main():
    global N
    
    A = [[0]*N for row in range(N)]
    B = [[0]*N for row in range(N)]
    
    for i in range(N):
        for j in range(N):
            A[i][j] = j + 1
    for i in range(N):
        for j in range(N):
            B[i][j] = -(j - 5)
    
    access_matrix(A, B)
    output_result(A, B)
    
main()
