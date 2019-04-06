for t in range(int(input())):
    n=int(input())
    s=input()
    temp=""
    c=0
    r="".join(set(s))
    temp=s.replace(r,"")
    print(r)
    print(temp)
    if(temp==s):
        print(s)
    else:
        for i in range(len(temp)):
            if(s[i]==temp[i]):
                c+=1
        if(c==len(temp)):
            print(temp)
