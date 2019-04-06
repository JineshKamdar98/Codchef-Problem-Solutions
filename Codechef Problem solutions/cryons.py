t=int(input())
while(t!=0):
    s=input()
    c=0
    for i in range(1,len(s)):
        if(s[i-1]!=s[i]):
            c+=1
    if(c%2==0):
        print(c//2)
    else:
        print((c//2)+1)
    t-=1
            
