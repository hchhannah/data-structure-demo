import sys

MAX = 10
cq = [""]*MAX
front = MAX-1
rear = MAX-1
tag = 0 
 
def enqueue_f():
    global MAX
    global cq
    global front
    global rear
    global tag
    
    if front == rear and tag == 1:
        print("佇列已滿")
    else:
        rear = (rear+1)%MAX
        cq[rear] = input("請輸入一筆資料(字串): ")
        if rear == front-1:
            tag == 1
    print()
    
def dequeue_f():
    global MAX
    global cq
    global front
    global rear
    global tag
    
    if front == rear and tag == 0:
        print("\n佇列為空")
    else:
        front = (front+1)%MAX
        print("\n %s 已被刪除" %cq[front])
        if rear == front:
            tag == 0
    print()
 
def list_f():
    global MAX
    global cq
    global front
    global rear
    global tag
    
    if rear == front and tag == 0:
        print("\n佇列為空\n")
    else:
        i = (front+1)%MAX
        print()
        while i != rear:
            print(cq[i])
            i = (i+1)%MAX
        print(cq[i])
        print()
        
def main():
    option = 0
    
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. List")
        print("4. Exit")
        
        try:
            option = int(input("請選擇要執行的項目: "))
        except ValueError:
            print("\nNot a correct number")
            print("try again\n")
            continue
        
        if option == 1:
            enqueue_f()
        elif option == 2:
            dequeue_f()
        elif option == 3:
            list_f()
        else:
            sys.exit(0)
            
main()
