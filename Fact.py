def fact(n):
    if n == 1:
        return 1 
    else:
        return n*fact(n-1)

def main():
    n = 10
    f = fact(n)
    print(f)
    
main()

