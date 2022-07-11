import sys

class Student:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.llink = None        
        self.rlink = None        

prev = None
current = None
ptr = None

head = Student()
#兩套環狀
head.llink = head
head.rlink = head

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
    
    #找到該插入的位置
    prev = head 
    current = head.rlink
    while current != head and current.score >= ptr.score:
        prev = current
        current = current.rlink
    #插入ptr，[][prev][] --> [][ptr][] --> [][current][] 
    ptr.rlink = current
    ptr.llink = prev
    prev.rlink = ptr
    current.llink = ptr
    
def display_f():
    global head
    global current
    
    count = 0
    
    if head.rlink == head:
        print("No student record\n")
    else: 
        current = head.rlink
        while current != head:
            print("%-17s %-15d" %(current.name, current.score))
            count += 1
            current = current.rlink
        print("total: %d\n" %count)
    
def delete_f():
    global current
    global prev
    global head
    
    del_name = ""
    
    if head.rlink == head:
        print("No student record\n")
    else:
        del_name = input("Delete student's name: ")
        #找出位置
        prev = head
        current = head.rlink
        while current != head and del_name != current.name:
            prev = current
            current = current.rlink
            
        if current != head:
            prev.rlink = current.rlink
            current.rlink.llink = prev
            current = None
            print("\nStudent %s record deleted\n" %del_name)
        else:
            print("\nStudent %s not found\n" %del_name)

def modify_f():
    global current
    global prev
    global head
    modify_name = ""
    
    if head.rlink == head:
        print("No student record\n")
    else:
        modify_name = input("Modify student's name: ")
        prev = head
        current = head.rlink
        while current != head and modify_name != current.name:
            prev = current
            current = current.rlink
        if current != head:
            prev.rlink = current.rlink
            current = None
            newscore = eval(input("Enter a new score: "))
            print()
            ptr.name = modify_name
            ptr.score = newscore            
            prev = head 
            current = head.rlink
            #成績高到低排列
            while current != head and current.score >= ptr.score:
                prev = current
                current = current.rlink
            #把插入的成績串在一起
            ptr.rlink = current
            ptr.llink = prev
            prev.rlink = ptr 
            current.llink = ptr
        else:
            print("\nStudent %s not found\n" %modify_name)    

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