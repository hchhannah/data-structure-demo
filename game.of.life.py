MAXROW = 10
MAXCOL = 25
DEAD = 0
ALIVE = 1
map_ = [ [DEAD for col in range(MAXCOL)] for row in range(MAXROW)]
newmap = [[DEAD for col in range(MAXCOL)] for row in range (MAXROW)]
generation = 0

def init():
    global MAXROW
    global MAXCOL
    global DEAD
    global ALIVE
    global map_
    global newmap
    row = 0
    col = 0
    print("Enter (x,y) where (x,y) is a living cell")
    print("0<=x<=%d, 0<=y<=%d" %(MAXROW-1,MAXCOL-1))
    print("terminate with (x,y) = (-1,-1)")

    while row!=-1 or col!=-1:
        row = int(input("x-->"))
        col = int(input("y-->"))
        if(0<=row and row<MAXROW and 0<=col and col<MAXCOL):
            map_[row][col] = ALIVE
        elif row == -1 and col == -1:
            print("input is terminated!")
        else: 
            print("(x,y) exceeds map range")

def output_map():
    global MAXCOL
    global MAXROW
    global map_
    global generation
    space = " "
    print(space, "\n Game of life status")
    generation += 1
    print("--------generation %d--------" %generation)
    for row in range(MAXROW):
        print()
        print(space)
        for col in range(MAXCOL):
            if map_[row][col] == ALIVE:
                print("@", end = "")
            else:
                print("-", end = "")

def Neighbors(row, col):
    global MAXCOL
    global MAXROW
    global map_
    global ALIVE
    
    count = 0
    
    for r in range(row-1, row+2):
        for c in range(col-1,col+2):
            if r<0 or r>=MAXROW or c<0 or c>=MAXCOL:
                continue
            if map_[r][c] == ALIVE:
                count += 1
                
    if map_[row][col] == ALIVE:
        count -= 1
    return count

def copymap():
    global MAXCOL
    global MAXROW
    global map_
    global newmap
    for row in range(MAXROW):
        for col in range(MAXCOL):
            map_[row][col] = newmap[row][col]

def access():
    global MAXCOL
    global MAXROW
    global DEAD
    global ALIVE
    global map_
    global newmap
    
    ans = 'y'
    while ans == 'y':
        for row in range(MAXROW):
            for col in range(MAXCOL):
                # print("%d, %d,%d"%(row,col,eighbors(row,col)))
                if Neighbors(row,col)<=1 or Neighbors(row,col)>=6:
                    newmap [row][col] = DEAD
                elif Neighbors(row,col)==2 or Neighbors(row,col)==3:
                    newmap [row][col] = map_[row][col]
                elif Neighbors(row,col)==4 or Neighbors(row,col)==5:
                    newmap [row] [col] = ALIVE
        copymap()
        while True:
            ans = input("\n\n continue? (y/n)")
            if ans == 'y' or ans == 'n':
                break
        if ans == 'y':
                output_map()

def main():
    init()
    output_map()
    access()
main()

