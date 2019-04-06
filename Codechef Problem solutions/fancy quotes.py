t=int(input())
while(t!=0):
    s=input()
    f=0
    for i in range(len(s)):
        if(i==0):
            if(s[i]=='n' and s[i+1]=='o' and s[i+2]==s[-1]=='t' and len(s)==3):
                f=1
                break
            elif(s[i]=='n' and s[i+1]=='o' and s[i+2]=='t' and s[i+3]==' '):
                f=1
                break
        elif(s[i]==' ' and s[i+1]=='n' and s[i+2]=='o' and s[i+3]==s[-1]=='t' and s[-2]=='o' and s[-3]=='n' and s[-4]==' '):
            f=1
            break
        elif(s[i]==' ' and s[i+1]=='n' and s[i+2]=='o' and s[i+3]=='t' and s[i+4]==' '):
            f=1
            break
    if(f==0):
        print("regularly fancy")
    else:
        print("Real fancy")
    t-=1        
