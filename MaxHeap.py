import sys

MAX = 100
heap_tree = [0] * MAX
last_index = 0

def insert_f():
    global MAX
    global last_index
    
    #MAX是100，[0]不用，所以99個就滿了，ex: [A,B,C], A的index=1
    if last_index >= MAX-1: 
        print("Heap is full")
        return
    
    id_temp = int(input("Please enter a number: "))
    create(id_temp)
    print("\nInsert successfully")

def create(id_temp):
    global last_index        
    global heap_tree        
    
    last_index += 1
    heap_tree[last_index] = id_temp
    adjust_u(heap_tree, last_index)

def adjust_u(temp, index):
    while index > 1:
        if temp[index] <= temp[index//2]:
           break
        else:
            exchange(temp, index, index//2)
        index//=2 #index = index // 2 
        
def exchange(arr, id1, id2):
    id_temp = arr[id1]
    arr[id1] = arr[id2]
    arr[id2] = id_temp
    
def delete_f():
    global last_index
    id_temp  = 0
    del_index = 0    
    
    if last_index < 1:
        print("No number to delete")
    else:
        id_temp = int(input("Please enter a number to delete: "))
        del_index = search(id_temp)
        if del_index == 0 :
            print("\nThe number not found")
        else:
            removes(del_index)
            print("\nThe number has been deleted")
                
def search(id_temp):
    global heap_tree
    global last_index
    
    for c_index in range(1, last_index+1):
        if id_temp == heap_tree[c_index]:
            return c_index
    return 0

def removes(index_temp):
    global last_index
    global heap_tree
    
    heap_tree[index_temp] = heap_tree[last_index]
    heap_tree[last_index] = 0
    last_index -= 1
    
    if last_index > 1:
        if heap_tree[index_temp] > heap_tree[index_temp//2] and index_temp > 1:
            adjust_u(heap_tree, index_temp)
        else:
            adjust_d(heap_tree, index_temp, last_index-1) #不寫-1也不會錯
 
def display_f():
    global last_index
    
    if last_index < 1:
        print("No number to show")
    else:
        print("1. increase")
        print("2. decrease")
        option = input("Please enter your option: ")
        print()
        show(option)

def show(option):
    global last_index
    global heap_tree
    
    heap_temp = []
    #tChart = ''
    
    heap_temp = [i for i in heap_tree] # = heap_tree.copy()
    print(heap_temp)
    c_index = last_index-1
    while c_index > 0 :
        exchange(heap_temp, 1, c_index+1)
        adjust_d(heap_temp, 1, c_index)
        c_index -= 1
    
    if option == "1":
        for c_index in range(1, last_index+1):
            print("", heap_temp[c_index])
    elif option == "2":
        c_index = last_index
        while c_index > 0:
            print("", heap_temp[c_index])
            c_index -= 1            

def adjust_d(temp, index1, index2):
    id_temp  = temp[index1]
    index_temp = index1*2
    while index_temp <= index2:
        if index_temp < index2 and temp[index_temp] < temp[index_temp+1]:
            index_temp += 1
        if id_temp >= temp[index_temp]:
            break
        else:
            temp[index_temp//2] = temp[index_temp]
            index_temp *= 2
        temp[index_temp//2] = id_temp
       
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