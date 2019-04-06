def diagonals(coord, size):
    limit = size - 1
    coords = []
    row = coord[0]
    col = coord[1]
    
    while row > 0 and col > 0:
        row -= 1
        col -= 1
        coords.append((row, col))

    row = coord[0]
    col = coord[1]

    while row < limit and col < limit:
        row += 1
        col += 1
        coords.append((row, col))

    row = coord[0]
    col = coord[1]

    while row < limit and col > 0:
        row += 1
        col -= 1
        coords.append((row, col))

    row = coord[0]
    col = coord[1]

    while row > 0 and col < limit:
        row -= 1
        col += 1
        coords.append((row, col))

    return coords

for t in range(int(input())):
    n=int(input())
    xnulist=[]
    ynulist=[]
    for i in range(n):
        x,y=map(int,input().split())
        xnulist.append(x)
        ynulist.append(y)
    a,b=map(int,input().split())
    if(a in xnulist):
        print("YES")
        continue
    elif(b in ynulist):
        print("YES")
        continue
    else:
        diag=diagonals((a,b),7)
        if((a,b) in diag):
            print("YES")
        else:
            print("NO")
        continue
            
        
        
    
