class Poly:
    def __init__(self):
        self.coef = 0 #係數
        self.exp = 0 #指數
        self.next = None
    
eq_h1 = None
eq_h2 = None
ptr = None
ans = None

def input_f():
    global ptr
    eq_h = None
    prev = None #尾部
    
    while True:
        ptr = Poly()
        
        try:
            ptr.coef = int(input("請輸入係數："))
        except ValueError:
            print("Not a correct number")
            print("Try again")
        
        if ptr.coef == 0:
            return eq_h

        try:
            ptr.exp = int(input("請輸入指數："))
        except ValueError:
            print("Not a correct number")
            print("Try again")
        
        if eq_h == None:
            eq_h = ptr
        else:
            prev.next = ptr #把新加入的數加在最後
        prev = ptr #prev = prev.next 把尾部往後指一個

def poly_add():
    global eq_h1
    global eq_h2 
    global ptr
    global ans
    
    this1 = eq_h1
    this2 = eq_h2    
    prev = None
    
    while this1 != None or this2 != None:
        ptr = Poly()
        #如果第二項跑完了但第一項還沒，或是第一項不是空的並且第一項的係數大於第二項的係數
        if (this1 != None and this2 == None) or this1 != None and this1.exp > this2.exp:
            #把第一項複製過來
            ptr.coef = this1.coef 
            ptr.exp = this1.exp
            #指標向後移動一格
            this1 = this1.next
        #第一項是空的從第二項複製
        elif this1 == None or this1.exp < this2.exp:
            ptr.coef = this2.coef
            ptr.exp = this2.exp
            this2 = this2.next
        #係數相等做相加
        else:
            ptr.coef = this1.coef + this2.coef
            ptr.exp = this1.exp
            if this1 != None:
                this1 = this1.next
            if this2 != None:
                this2 = this2.next
        
        #如果係數是負的加起來有可能是0
        if ptr.coef != 0:
            #是第一項的話整個答案還是空的
            if ans == None:
                ans = ptr
            else:
                prev.next = ptr
            prev = ptr
        else:
            #是0的話就把值清掉進入下一個迴圈
            ptr = None
                
def show_poly(head, text):
    node = head
    print("\n%s" %text, end="")
    while node != None:
        print("%dx^%d" % (node.coef, node.exp), end="")
        if node.next != None and node.next.coef >= 0: #下一個不是空的然後係數不是0
            print("+", end="")
        node = node.next
    print()

def main():
    global eq_h1
    global eq_h2 
    global ans
    
    print("\n輸入第一個多項式(若輸入的係數為0，則停止)")
    eq_h1 = input_f()
    print("\n輸入第二個多項式(若輸入的係數為0，則停止)")
    eq_h2 = input_f()
    poly_add()
    show_poly(eq_h1, "第一個多項式：")
    show_poly(eq_h2, "第二個多項式：")
    show_poly(ans, "相加結果：")
    
main()
        

