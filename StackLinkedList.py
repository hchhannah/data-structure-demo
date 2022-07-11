class Node:
    def __init__(self):
        self.data = ""
        self.next = None

top = None
ptr = None

def push_f():
    global top 
    global ptr
    ptr = Node()
    ptr.data = input("Enter a string: ")
    ptr.next = top #把ptr.next指向top現在的位置
    top = ptr #再把top改指向ptr現在的位置 
    print()
    
def pop_f(): 
    global top 
    global ptr
    
    if top == None:
        print("Stack is empty") 
    else:
        ptr = top
        del_data = ptr.data
        top = top.next
        ptr = None
        print("%s has been deleted" %del_data)
    print()

def list_f():
    global top 
    global ptr
    count = 0
    
    if top == None:
        print("Stack is empty")
    else:
        ptr = top
        while ptr != None:
            print(ptr.data)
            count += 1
            ptr = ptr.next
        print("Total: %d" %count)
    print() 

def main():
    option = 0 
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. List")
        print("4. Exit")
        
        try:
            option = int(input("Choice: "))
        except ValueError:
            print("Not a correct number")
            print("Try again\n")
        print()
        
        if option == 1:
            push_f()
        elif option == 2:
            pop_f()
        elif option == 3:
            list_f()
        elif option == 4:
            break
main()



