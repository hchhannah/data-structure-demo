import sys
class Student:    
    def __init__(self):
        self.name = ""
        self.score = 0
        self.next = None
        
ptr = None
current = None
prev = None

head = Student()
head.next = head #循環

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
    while current != head and current.score >= ptr.score: #成績高排到低
        #找出該插入的位置
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
    
    if head.next == head:
        print("No student record\n")
    else:
        del_name = input("Delete student's name: ")
        #從頭找出位置
        prev = head
        current = head.next
        while current != head and del_name != current.name:
            prev = current
            current = current.next
            
        if current != head: 
            #越過current指向下一個後清空current的記憶體
            prev.next = current.next
            current = None
            print("\nStudent %s record deleted\n" %del_name)
        else:
            print("\nStudent %s not found\n" %del_name)

def modify_f():
    global ptr
    global current
    global prev
    global head

    modify_name = ""
    
    if head.next == head:
        print("No student record\n")
    else:
        modify_name = input("Modify student's name: ")
        #從頭找出位置
        prev = head 
        current = head.next
        while current != head and modify_name != current.name:
            prev = current
            current = current.next
        if current != head:
            prev.next = current.next
            current = None
            newscore = eval(input("Enter a new score: "))
            print()
            ptr.name = modify_name
            ptr.score = newscore   
            #把更改後的成績插入正確位置(高排到低)
            prev = head 
            current = head.next
            while current != head and current.score >= ptr.score:
                prev = current
                current = current.next
            ptr.next = current
            prev.next = ptr 
        else:
            print("\nStudent %s not found\n" %modify_name)
            
def display_f():
    global head
    global current
    count = 0
    if head.next == head:
        print("No student record\n")
    else:
        current = head.next
        while current != head: #如果重疊到head代表繞一圈了
            print("%-17s %-15d" %(current.name, current.score))
            count += 1
            current = current.next
        print("total: %d\n" %count)

def main():
    while True:
        print("1.Insert")
        print("2.Delete")
        print("3.Modify")
        print("4.Display")
        print("5.Exit")
        
        try:
            option = int(input("Choice: "))
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


