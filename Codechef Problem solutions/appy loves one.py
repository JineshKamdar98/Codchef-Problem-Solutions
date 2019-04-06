n,q,k=input().split()
n,q,k=int(n),int(q),int(k)
a=list(map(int,input().split()[:n]))
s=input()
for i in s:
    #print(a)
    if(i=='?'):
        #print(1)
        result=0
        c=0
        for j in a:
            #print(result)
            if(j==0):
                c=0
            else:
                c+=1
                result=max(result,c)
        if(result<=k):
            print(result)
        else:
            print(k)
    elif(i=='!'):
        #print(2)
        a.insert(0,a.pop())
            
