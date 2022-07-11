import sys

MAX = 20
st = [""]*MAX
top = -1

def push_f():
    global MAX
    global st
    global top
    if top >= MAX-1:
        print("堆疊已滿")
    else:
        top+=1
        st[top] = input("請輸入一筆資料(字串)")
    print()

def pop_f():
    global st
    global top
    if top < 0:
        print("堆疊為空")
    else:
        print("\n %s 已被刪除" %st[top])
        top -= 1
    print()

def list_f():
    global st
    global top
    
    if top < 0:
        print("堆疊為空")
    else:
        i = top
        while i >= 0:
            print(st[i])
            i -= 1
    print()
           
def main():
    
    option = 0
    
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. List")
        print("4. Exit")
        
        option = eval(input("請選擇要執行的項目"))
    
        
        if option != 1 and option != 2 and option != 3 and option != 4:
            print("Not a correct number")
            print("try again")
            
        #try:
        #    option = eval(input("請選擇要執行的項目"))
        #except ValueError:
        #    print("Not a correct number")
        #    print("try again")
        
        if option == 1:
            push_f()
        elif option == 2:
            pop_f()
        elif option == 3:
            list_f()
        else:
            sys.exit(0)
main()
