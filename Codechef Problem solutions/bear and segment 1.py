t=int(input())
while(t!=0):
    s=input()
    f=0
    k=0
    for i in range(0,len(s)):
        if(s[i]=='1'):
            k+=1
    for i in range(1,len(s)):
        if(s[i-1]=='1' and s[i]=='0'):
            for j in range(i+1,len(s)):
                if(s[j]=='1'):
                    f=1
                    break
        if(f==1):
            break
    if(f==1 or k==0):
        print('NO')
    else:
        print('YES')
    t-=1
