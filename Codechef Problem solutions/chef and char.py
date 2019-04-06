t=int(input())
while(t!=0):
    s=input()
    c=0
    for i in range(0,len(s)):
        if(s[i]=='c' or s[i]=='h' or s[i]=='e' or s[i]=='f'):
            if((s[i+1]=='c' or s[i+1]=='h' or s[i+1]=='e' or s[i+1]=='f') and s[i+1]!=s[i]):
                if((s[i+2]=='c' or s[i+2]=='h' or s[i+2]=='e' or s[i+2]=='f') and s[i+2]!=s[i+1] and s[i+2]!=s[i]):
                    if((s[i+3]=='c' or s[i+3]=='h' or s[i+3]=='e' or s[i+3]=='f') and s[i+3]!=s[i+2] and s[i+3]!=s[i+1] and s[i+3]!=s[i]):
                        c+=1
    if(c!=0):
        print("lovely",c)
    else:
        print("normal")
    t=t-1
