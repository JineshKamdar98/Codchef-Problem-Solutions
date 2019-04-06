n,m=map(int,input().split())
pelu=[]
biju=[]
for i in range(m):
    u,v=map(int,input().split())
    pelu.append(u)
    biju.append(v)
c=0
for j in biju:
    if j in pelu:
        continue
    else:
        c+=1
        if(c==1):
            i1=biju.index(j)
        elif(c==2):
            i2=biju.index(j)
            c=0
        pelu.remove(i1)
        pelu.remove(i2)
        biju.remove(i1)
        biju.remove(i2)
            

    
