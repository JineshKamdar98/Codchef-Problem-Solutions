for t in range(int(input())):
    n,m,x,y=input().split()
    n,m,x,y=[int(n),int(m),int(x),int(y)]
    k,p=1,1
    if(k==n-1 and p==m-1):
        print('Chefirnemo')
    else:
        k,p=1,1
        while(k<n):
            if(k==n-1):
                break
            k+=x
            #print('w1')
        while(p<m):
            if(p==m-1):
                break
            p+=y
            #print('w2')
        #print(k,p)
        if(k==n and p==m):
            print('Chefirnemo')
        elif((k==n and p>m) or (p==m and k>n) or (k>n and p>m) or (k>n and p<m) or (p>m and k<n)):
            print('Pofik')
        elif((k==n-1 and p!=m-1) or (k!=n-1 and p==m-1)):
            print('Pofik')
        elif(k==n-1 and p==m-1):
            print('Chefirnemo')
    
            
