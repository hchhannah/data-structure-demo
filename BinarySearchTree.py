import sys

class Student:
    name = ""
    score = 0
    llink = None
    rlink = None

root = None

def insert_f():
    print("insert data")
    name = input("Enter student's name: ")
    score = eval(input("Enter student's score: "))
    access(name, score)

def access(name, score):
    global root
    node = None
    prev = None
    
    #不是空的代表已經有這筆資料了
    if search(name) != None:
        print("Student %s has existed" %name)
        return
    
    ptr = Student()
    ptr.name = name
    ptr.score = score
    
    #第一個輸入的是root
    if root == None:
        root = ptr
    #找出該插入的位置
    else:
        node = root
        while node != None:
            prev = node #先指向一個地方
            if ptr.name < node.name:
                node = node.llink
            else:
                node = node.rlink
        #prev現在是指向一個leaf node，判斷ptr要插在哪
        if ptr.name < prev.name:
            prev.llink = ptr
        else:
            prev.rlink = ptr

def search(target):
    global root
    node = root 
    
    while node != None:
        #找到一樣的名字
        if target == node.name:
            return node
        #沒有一樣的-->排序順序
        elif target < node.name:
            node = node.llink
        else:
            node = node.rlink
    return node #=return none

def delete_f():
    global root
    if root == None:
        print("No student record")
        return
    name = input("Enter student's name: ")
    removing(name)

def removing(name):
    global root
    del_node = search(name)
    
    if del_node == None:
        print("Student %s not found" %name)
        return
    
    if del_node.llink != None or del_node.rlink != None:
        del_node = replace(del_node)
    else:
        #把樹根刪掉=把整棵樹砍掉
        if del_node == root:
            root = None
        #(del_node沒有子節點，所以parent繞過他指向空)
        else:
            connect(del_node, "n")
    del_node = None
    
    print("\nStudent %s has been deleted" %name)
     
def replace(node):
    re_node = None
    re_node = search_replace_rlink(node.rlink)
    
    if re_node == None:
        re_node = search_replace_llink(node.llink)
    
    if re_node.rlink != None:
        connect(re_node, "r") #'r' = replace_node.rlink
    elif re_node.llink != None:
        connect(re_node, "l")
    else:
        connect(re_node, "n")
        
    node.name = re_node.name
    node.score = re_node.score
    return re_node
        
def search_replace_rlink(node): #在右子樹裡往左找最小的
    re_node = node
    
    while re_node != None and re_node.llink != None: #往左邊找
        re_node = re_node.llink
    return re_node

def search_replace_llink(node):#在左子樹裡往右找最大的
    re_node =node
    
    while re_node != None and re_node.rlink != None:
        re_node = re_node.rlink
    return re_node

def connect(node, link):
    parent =search_p(node)
    if node.name < parent.name:
        #拿parent的llink改指到node的rlink
        if link == "r":
            parent.llink = node.rlink
        elif link == "l":
            parent.llink = node.llink
        else:
            parent.llink = None
    else:
        if link == "r":
            parent.rlink = node.rlink
        elif link == "l":
            parent.rlink = node.llink
        else:
            parent.rlink = None
        
def search_p(node):
    global root
    parent = root
    
    while parent != None:
        #node在parent的左子樹
        if node.name < parent.name:
            #剛好指到父節點
            if node.name == parent.llink.name:
                return parent
            else:
                #向左滑動一格
                parent = parent.llink
        #node在parent的右子樹
        else:
            if node.name == parent.rlink.name:
                return parent
            else:
                parent = parent.rlink
    return None

def modify_f():
    global root
    
    if root == None:
        print("No student record")
        return
    name = input("Enter student's name: ")
    node = search(name) #找到位置
    
    if node == None:
        print("Student %s not found" %name)
    else:
        print("Current score: %d" %node.score)
        node.score = eval(input("Enter a new score: "))
        print("Student %s has been modified" %name)
    
def display_f():
    global root
    
    if root == None:
        print("No student record")
        return
    print("===== Student data =====")
    inorder(root)

def inorder(node): 
    if node != None:
        inorder(node.llink)
        print("%-15s %-3d" % (node.name, node.score))
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