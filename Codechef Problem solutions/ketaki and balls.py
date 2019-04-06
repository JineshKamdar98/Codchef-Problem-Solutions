for _ in range(int(input())):
    n=int(input())
    s=input()
    i=1
    c=0
    while(i<n):
        if(s[i]=='R' and s[i-1]=='B'):
            c+=1
            i+=1
        elif(s[i]=='B' and s[i-1]=='R'):
            c+=1
            i+=1
        i+=1
    print(c)
        
