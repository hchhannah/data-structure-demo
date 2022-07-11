A = [[1,3,5],[7,9,11],[13,15,17]]
B = [[9,8,7],[6,5,4],[3,2,1]]
N = 3
C = [[None] * N for row in range(N)]

for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]

print('[矩陣A和矩陣B相加的結果]')

for i in range(3):
    for j in range(3):
        print('%d' %C[i][j], end='\t')
    print()
