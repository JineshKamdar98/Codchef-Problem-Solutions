t=int(input())
while(t!=0):
    r,c,k=input().split()
    r,c,k=[int(r),int(c),int(k)]
    if((r==1 and c==1)||(r==1 and c==8)||(r==8 and c==1)||(r==8 and c==8)):
        print((k+1)**2)
    elif((r==1 and c!=1 and c!=8)or(r==8 and c!=1 and c!=8)or(c==1 and r!=1 and r!=8)or(c==8 and r!=1 and r!=8)):
        print(2*((k+1)**2)-(k+1))
    else:
        print(((2*k)+1)**2)
    t-=1
