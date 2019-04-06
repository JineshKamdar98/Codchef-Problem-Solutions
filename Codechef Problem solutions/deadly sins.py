t=int(input())
while(t!=0):
    x,y=input().split()
    x,y=[int(x),int(y)]
    while(x!=y):
        if(x>y):
            if(x%y!=0):
                x=x%y
            else:
                print(2*y)
                break
        if(x<y):
            if(y%x!=0):
                y=y%x
            else:
                print(2*x)
                break
        if(x==0 or y==0):
            print(x+y)
            break
    if(x==y):
        print(x+y)
    t=t-1
        
