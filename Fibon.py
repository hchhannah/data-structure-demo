def fibon(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibon(n-2)+fibon(n-1)
        
def main():
    n = int(input("輸入:"))
    f = fibon(n)
    print(f)
    
main()


