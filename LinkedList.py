class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        
x = Node()
x.data = 9

y = Node()
y.data = 8
y.next = x

z = Node()
z.data = 7
z.next = y

temp = z

while temp != None:
    print(temp.data)
    temp = temp.next #後移一格
    