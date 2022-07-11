import sys

class TreeNode:
    def __init__(self):
        self.ID = 0
        self.n = 0 
        self.key = [0]*3
        self.link = [None]*3

MAX = 3
ptr = None
root = None
node = None
prev = None
parent = None
replace = None
id_seq = ''

def insert_f():
    add_num = int(input("\nPlease enter a number: "))
    create(add_num)
    print()
    
def create(num):
    global root
    global ptr
    global node
    global prev
    
    ans = 0
    i = 0
    
    if root == None:
        initial()
        ptr.key[1] = num
        ptr.n += 1
        root = ptr
    else:
        ans = search_num(num)
        if ans != 0 :
            print("Number %d has existed\n" % num)
            return
        else:
            node = search_node(num)
            if node != None:
                i = 1
                while i < MAX-1:
                    if num < node.key[i]:
                        break
                    i += 1
                moveright(i, num)
            else:
                initial()
                ptr.key[1] = num
                ptr.n += 1 
                i = 1
                while i < MAX:
                    if num < prev.key[i]:
                        break
                    i += 1
                prev.link[i-1] = ptr
    print("\n%d has been inserted" % num)

def search_num(num):
    global root
    global parent
    global node
    global prev
    
    #n_temp = 0 
    
    node = root
    while node != None:
        parent = prev 
        prev = node
        i = 1 
        done = 0
        while i <= node.n:
            if num == node.key[i]:
                return i 
            if num < node.key[i]:
                node = node.link[i-1]
                done = 1
                break
            i += 1
        if done == 0:
            node = node.link[i-1]
    return 0
            

def search_node(num):
    global MAX
    global root
    
    node_temp = root
    
    while node_temp != None:
        if node_temp.n < MAX-1:
            return node_temp
        else:
            i = 1
            done = 0
            while i < MAX:
                if node_temp.n < i:
                    break
                if num < node_temp.key[i]:
                    node_temp = node_temp.link[i-1]
                    done = 1
                    break
                i += 1
            if done == 0 :
                node_temp = node_temp.link[i-1]
    return node_temp

def moveright(index, num):
    global node
    
    i = node.n + 1
    
    while i > index:
        node.key[i] = node.key[i-1]
        node.link[i] = node.link[i-1]
        i -= 1
    node.key[i] = num
    if node.link[i-1] != None and node.link[i-1].key[1] > num:
        node.link[i] = node.link[i-1]
        node.link[i-1] = None
    node.n += 1

def initial():
    global MAX
    global ptr
    
    ptr = TreeNode()
    for i in range(MAX):
        ptr.link[i] = None
    ptr.n = 0

def delete_f():
    global root
    global node
    
    del_num = 0
    ans = 0
    
    if root == None:
        print("\nNo data found\n")
    else:
        del_num = int(input("Enter delete number: "))
        ans = search_num(del_num)
        if ans == 0:
            print("\nNumber not found\n")
        else:
            removes(node, ans)
            print("\nNumber %d has been deleted\n" %del_num)

def removes(node_temp, location):
    global root
    global node
    global prev
    global parent
    global replace
    
    node = node_temp
    replace = find_next(node.link[location])
    if replace == None:
        replace = find_prev(node.link[location-1])
        if replace == None:
            moveleft(location)
            replace = node
            if node.n == 0:
                if node == root:
                    root = None
                else:
                    for i in range(parent):
                        if node == parent.link[i]:
                            parent.link[i] = None
                            break
        else:
            node.key[location] = replace.key[replace.n]
            parent = prev 
            removes(replace, replace.n)
    else:
        node.key[location] = replace.key[1]
        parent = prev
        removes(replace, 1)
        
    
def find_next(node_temp):
    global node
    global prev
    prev = node
    
    if node_temp != None:
        while node_temp.link[0] != None:
            prev = node_temp
            node_temp = node_temp.link[0]
    return node_temp
    
def find_prev(node_temp):
    global node
    global prev
    global MAX
    
    prev = node
    if node_temp != None:
        while node_temp.link[MAX-1] != None:
            prev = node_temp
            node_temp = node_temp.link[MAX-1]
    return node_temp

def moveleft(index):
    global node
    
    for i in range(index, node.n):
        node.key[i] = node.key[i+1]
        node.link[i] = node.link[i+1]
    node.n-=1
    

def display_f():
    global root
    global id_seq
    
    if root == None:
        print("\nNo data found!!\n")
    else:
        id_seq = "a"
        preorder_id(root)
        print("\nThe data of M-way search tree is listing below: ")
        print("========================================")
        preorder_num(root)
        print("========================================")

def preorder_id(tree):
    global id_seq
    
    if tree != None:
        tree.ID = id_seq
        id_seq = chr(ord(id_seq) + 1)
        for i in range(tree.n+1):
            preorder_id(tree.link[i])
    
def preorder_num(tree):
    i = 0
    link_id = ""
    
    if tree != None:
        if tree.link[0] == None:
            link_id = "0"
        else:
            link_id = tree.link[0].ID
        print("%s, %d, %s" %(tree.ID, tree.n, link_id), end = "")
        for i in range(1, tree.n+1):
            if tree.link[i] == None:
                link_id = "0"
            else:
                link_id = tree.link[i].ID
            print(", (%d, %s)" % (tree.key[i], link_id), end = "")
            i += 1
        print()
        for i in range(tree.n+1):
            preorder_num(tree.link[i])
def main():
    
    while True:
        print()
        print("1.Insert")
        print("2.Delete")
        print("3.Display")
        print("4.Exit")
        
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
            display_f()
        elif option == 4:            
            sys.exit(0)

main()