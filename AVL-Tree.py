import sys

class Student:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.score = 0
        self.bf = 0
        self.llink = None
        self.rlink = None

root = None
pivot = None
pivot_prev = None
ptr = None
current = None
prev = None
node_count = 0        
        
        
def insert_f():
    global node_count
    
    id_t = eval(input("Student id: "))
    name_t = input("Student name: ")
    score_t = eval(input("Student score: "))
    node_count += 1
    sort_f(id_t, name_t, score_t)
    
def sort_f(id_t, name_t, score_t):
    global ptr
    global root
    global current
    global prev
    global pivot
    
    current = root
    
    while current != None and id_t != current.id:
        if id_t < current.id:
            prev = current
            current = current.llink
        else:
            prev = current 
            current = current.rlink
    
    if current == None or id_t != current.id:
        ptr = Student()
        ptr.id = id_t
        ptr.name = name_t
        ptr.score = score_t
        
        if root == None:
            root = ptr
        elif ptr.id < prev.id:
            prev.llink = ptr
        else:
            prev.rlink = ptr
        
        bf_count(root)
        pivot = pivot_find()
        
        if pivot != None:
            op = type_find()
            if op == 11:
                type_ll()
            elif op == 22:
                type_rr()
            elif op == 12:
                type_lr()
            elif op == 21:
                type_rl()
        bf_count(root)
    else:
        print("Student %s has existed" %(id_t))
        
            
def bf_count(trees):
    if trees != None:
        bf_count(trees.llink)
        bf_count(trees.rlink)
        trees.bf = height_count(trees.llink) - height_count(trees.rlink)

def height_count(trees):
    if trees == None:
        return 0 
    elif trees.llink == None and trees.rlink == None:
        return 1
    elif height_count(trees.llink) > height_count(trees.rlink):
        return 1 + height_count(trees.llink)
    else:
        return 1 + height_count(trees.rlink)

def pivot_find():
    global root
    global prev
    global current
    global pivot
    global pivot_prev
    global node_count
    
    current = root
    pivot = None
    
    for i in range(node_count):
        if current.bf < -1 or current.bf > 1:
            pivot = current
            if pivot != root:
                pivot.prev = prev
        if current.bf > 0 :
            prev = current
            current = current.llink
        elif current.bf < 0:
            prev = current
            current = current.rlink
    return pivot

def type_find():
    global current
    global pivot
    
    op_r = 0
    current = pivot
    
    for i in range(2):
        if current.bf > 0:
            if op_r == 0:
                op_r += 10
            else:
                op_r += 1
        elif current.bf < 0:
            if op_r == 0:
                op_r += 20
            else:
                op_r += 2
    
    return op_r
    
def type_ll():
    global root
    global pivot
    global pivot_prev
    
    pivot_next = pivot.llink
    temp = pivot_next.rlink
    
    pivot_next.rlink = pivot
    pivot.llink = temp
    
    if pivot == root:
        root = pivot_next
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = pivot_next
    else:
        pivot_prev.rlink = pivot_next

def type_rr():
    global root
    global pivot
    global pivot_prev
    
    pivot_next = pivot.rlink
    temp = pivot_next.llink
    
    pivot_next.llink = pivot
    pivot.rlink = temp
    
    if pivot == root:
        root = pivot_next
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = pivot_next
    else:
        pivot_prev.rlink = pivot_next
        
def type_lr():
    global root
    global pivot
    global pivot_prev
    
    pivot_next = pivot.llink
    temp = pivot_next.rlink
    
    pivot.llink = temp.rlink
    pivot_next.rlink = temp.llink
    
    temp.llink = pivot_next
    temp.rlink = pivot
    
    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp

def type_rl():
    global root
    global pivot
    global pivot_prev
    
    pivot_next = pivot.rlink
    temp = pivot_next.llink
    
    pivot.rlink = temp.llink
    pivot_next.llink = temp.rlink
    
    temp.rlink = pivot_next
    temp.llink = pivot
    
    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp

def delete_f(): #第六章的刪除加上insert一小段
    global root
    global current
    global prev
    global pivot
    global node_count
    
    clear = None
    
    if root == None:
        print("\n No studetnt record exist")
    else:
        id_t = eval(input("Enter student id: "))
        tempn = id_t
        current = root
        
        while current != None and id_t != current.id:
            if id_t < current.id:
                prev = current
                current = current.llink
            else:
                prev = current
                current = current.rlink
                
        if current != None and id_t == current.id:
            if current.llink == None and current.rlink == None:
                clear = current
                if id_t == root.id:
                    root = None
                else:
                    if id_t < prev.id:
                        prev.llink = None
                    else:
                        prev.rlink = None
                clear = None
            else:
                if current.llink != None:
                    clear = current.llink
                    while current.rlink != None:
                        prev = clear
                        clear = clear.rlink
                    current.id = clear.id
                    current.score = clear.score
                    if current.llink == clear:
                        current.llink = clear.llink
                    else:
                        prev.rlink = clear.llink
                else:
                    clear = current.rlink
                    while current.llink != None:
                        prev = clear
                        clear = clear.llink
                    current.id = clear.id
                    current.score = clear.score
                    if current.rlink == clear:
                        current.rlink = clear.rlink
                    else:
                        prev.llink = clear.rlink
                clear = None
            bf_count(root)
            
            if root != None:
                pivot = pivot_find()
                while pivot != None:
                    op = type_find()
                    if op == 11:
                        type_ll()
                    elif op == 22:
                        type_rr()
                    elif op == 12:
                        type_lr()
                    elif op == 21:
                        type_rl()
                    bf_count(root)
                    pivot = pivot_find() 
            node_count -= 1
            print('\nStudent %s has been deleted!' %tempn)
        else:
            print('\nStudent %s not found!'  %tempn)        
                
def modify_f():#名字跟分數可以改
    global root
    global current
    
    if root == None:
        print("\n No student record exist")
    else:
        id_t = eval(input("Student id: "))
        
        current = root
        while current != None and id_t != current.id:
            if id_t < current.id:
                current = current.llink
            else:
                current = current.rlink
        
        if current != None:
            print("\nStudent id: ", current.id)
            print("Student name: ", current.name)
            print("Student score: ", current.score)
            print("\n========================")
            print("\n1. Modify name")
            print("2. Modify score")
            option = eval(input("Enter your option: "))
            if option == 1:
                current.name = input("Enter new student name: ")
                print("\nData updated successfully")               
            elif option == 2:
                current.score = eval(input("Enter a new score: "))
                print("\nData updated successfully")   
            print("========================")   
            print("Student id: ", current.id)
            print("Student name: ", current.name)
            print("Student score: ", current.score)
        else:
            print("\nStudent %d not found" %(id_t))

def display_f():
    global root
    
    if root == None:
        print("No student record")
        return
    print("======== Student data ========")
    inorder(root)

def inorder(node): 
    if node != None:
        inorder(node.llink)
        print("%-10s %-15s %-3d" % (node.id, node.name, node.score))
        inorder(node.rlink)
    

def main():
    while True:
        print()
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