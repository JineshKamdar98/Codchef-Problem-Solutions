for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    pos=0
    neg=0
    zr=0
    for i in a:
        if(i<0):
            neg+=1
        elif(i>0):
            pos+=1
        else:
            zr+=1
    if(pos>neg and pos!=n):
        print(pos+zr,neg)
    elif(neg>=pos and neg!=n):
        print(neg+zr,pos)
    else:
        if(pos==n):
            print(pos,pos)
        elif(neg==n):
            print(neg,neg)
