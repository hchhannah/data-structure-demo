import sys

class Student:    
    def __init__(self):
        self.name = ""
        self.score = 0
        self.next = None
        
ptr = None
current = None
prev = None
option = None

head = Student()
head.next = None

def insert_f():
    global ptr
    global current
    global prev
    global head
    
    ptr = Student()
    ptr.next = None
    ptr.name = input("Student's name: ")
    ptr.score = eval(input("Student's score: "))
    print() 
    
    prev = head 
    current = head.next 
    while current != None and current.score >= ptr.score: #找出該插入的位置
        prev = current 
        current = current.next 
    #做插入動作 [head][] --> [prev][] --> [ptr][] --> [current][]
    ptr.next = current 
    prev.next = ptr

def delete_f():
    global current 
    global prev
    global head
    
    del_name = ""
    
    if head.next == None: 
        print("No student record\n")
    else:
        del_name = input("Delete student's name: ")
        #移到頭
        prev = head
        current = head.next
        while current != None and del_name != current.name: #從頭開始找名字
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next #prev繞過current指向current的下一個節點
            current = None #釋放current
            print("\nStudent's %s record deleted\n" %del_name)
        else: #如果跑完了current是空的代表沒找到
            print("\nStudent %s not found\n" %del_name)

def modify_f():
    global ptr
    global current
    global prev
    global head
    
    modify_name = ""
    
    if head.next == None:
        print("No student record\n")
    else:
        modify_name = input("Modify student's name: ")
        prev = head
        current = head.next 
        while current != None and modify_name != current.name: #從頭開始找名字
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next
            current = None
            newscore = eval(input("Enter a new score: "))
            print()
            ptr.name = modify_name
            ptr.score = newscore            
            prev = head 
            current = head.next
            while current != None and current.score >= ptr.score: #跟insert一樣
                prev = current
                current = current.next
            ptr.next = current
            prev.next = ptr
        else: #如果跑完了current是空的代表沒找到
            print("Student %s not found\n" % modify_name)
            
def display_f():
    global head
    global current
    count = 0 
    if head.next == None: #鏈結是空的
        print("No student record\n")
    else:
        current = head.next
        while current != None:
            print("%-17s %-15d" %(current.name, current.score))
            count += 1
            current = current.next
        print("total: %d\n" %count)

def main():
    global option
    
    while True:
        print("1.Insert")
        print("2.Delete")
        print("3.Modify")
        print("4.Display")
        print("5.Exit")
        
        try:
            option = eval(input("Choice: "))
        except ValueError:
            print("Not a correct number")
            print("Try again\n")
        
        print()
        if option == 1:
            insert_f()
        elif option == 2:
            delete_f()
        elif option == 3:
            modify_f()
        elif option == 4:
            display_f()
        elif option == 5:
            sys.exit(0)
        
main()



