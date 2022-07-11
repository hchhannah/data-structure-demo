str_ = ""
MAX = 20
infix_q = [""] * MAX

def infix_to_postfix():
    global MAX
    global infix_q
    global str_
    
    
    top = i = 0
    index = -1
    stack_t = [""] * MAX 
    
    while i<len(str_):
        index += 1
        infix_q[index] = str_[i]
        i+=1
        
    infix_q[index+1] = "#"
    stack_t[top] = "#"
    
    for ctr in range(index+2):
        if infix_q[ctr]==")":
            while stack_t[top] !="(":
                print(stack_t[top], end ="")
                top -= 1
            top -= 1
        elif infix_q[ctr]=="#":
            while stack_t[top] !="#":
                print(stack_t[top], end ="")
                top -= 1
        elif infix_q[ctr] == "("\
            or infix_q[ctr] == "^"\
            or infix_q[ctr] == "*"\
            or infix_q[ctr] == "/"\
            or infix_q[ctr] == "+"\
            or infix_q[ctr] == "-":
                while compare(stack_t[top], infix_q[ctr]) == 1:
                    print(stack_t[top], end="")
                    top -= 1
                top += 1
                stack_t[top] = infix_q[ctr]
        else:
            print(infix_q[ctr], end="")
            
def compare(stack_o, infix_o):
    infix_priority = []
    stack_priority = []
    index_s = 0
    index_i = 0
    
    infix_priority.append("#")
    infix_priority.append(")")
    infix_priority.append("+")
    infix_priority.append("-")
    infix_priority.append("*")
    infix_priority.append("/")
    infix_priority.append("^")
    infix_priority.append(" ")
    infix_priority.append("#")
    infix_priority.append("(")
    
    stack_priority.append("#")
    stack_priority.append("(")
    stack_priority.append("+")
    stack_priority.append("-")
    stack_priority.append("*")
    stack_priority.append("/")
    stack_priority.append("^")
    stack_priority.append(" ")
    
    while stack_priority[index_s] != stack_o:
        index_s += 1
    
    while infix_priority[index_i] != infix_o:
        index_i += 1
    
    if (index_s//2) >= (index_i//2):
        return 1
    else:
        return 0

def main():
    global str_
    print("^: 次方 \n*: 乘 \n/: 除 \n+: 加 \n-: 減 \n(: 左括號\n): 右括號")
    str_ = str(input("輸入一個中序算式: "))
    infix_to_postfix()
    
main()