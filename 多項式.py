DUMMY = -1

def Padd(a, b, c):
    p = q = r = m = n = 0 
    result = ''
    
    m = a[1]
    n = b[1]
    p = q = r = 2
    
    while p<= 2*m and q <= 2*n:
        result = compare(a[p], b[q])
        
        if result == "=":
            c[r+1] = a[p+1] + b[q+1]
            if c[r+1] != 0:
                c[r] = a[p]
                r += 2
            p += 2
            q += 2
        elif result == ">":
            c[r+1] = a[p+1]
            c[r] = a[p]
            p += 2
            r += 2
        elif result == "<":
            c[r+1] = b[q+1]
            c[r] = b[q]
            q += 2
            r += 2
    
    while p <= 2*m:
        c[r+1] = a[p+1]
        c[r] = a[p]
        p += 2
        r += 2
        
    while q <= 2*m:
        c[r+1] = b[q+1]
        c[r] = b[q]
        q += 2
        r += 2
    
    c[1] = r // 2 - 1   
                 
def compare(x, y):
    if x == y:
        return "="
    elif x > y:
        return ">"
    else:
        return "<"
    
def output_P(p, n):
    i = 0
    print('(', end = '')
    for i in range(1, n+1):
        print('%d' % p[i], end = '')
    print(')', end = '')
    
def main():
    global DUMMY
    
    A = []
    B = []
    
    A.append(DUMMY)
    A.append(3)
    A.append(4)
    A.append(5)
    A.append(2)
    A.append(3)
    A.append(0)
    A.append(2)
    
    B.append(DUMMY)
    B.append(3)
    B.append(3)
    B.append(6)
    B.append(2)
    B.append(2)
    B.append(0)
    B.append(1)
    
    C = [0]*12
    
    Padd(A, B, C)
    
    print('\nA = ', end = '')
    output_P(A, A[1]*2 +1)
    print('\nB = ', end = '')
    output_P(B, B[1]*2 +1)
    print('\nC = ', end = '')
    output_P(C, C[1]*2 +1)

main()

