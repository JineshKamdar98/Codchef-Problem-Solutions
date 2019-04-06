from math import gcd as bltin_gcd
#import random

#primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    flag=0
    i=1
    while((i<n)and(bltin_gcd(a[0],a[i])==1)):
        i+=1
    if(i==n):
        flag=0
    else:
        flag=1
        if(a[0]==47):
            a[i]=43
        else:
            a[i]=47
    print(flag)
    for k in a:
        print(k,end=' ')
    print()































    
    '''if(bltin_gcd(a[0],a[n-1])!=1):
        if(a[0] not in primes and bltin_gcd(a[0],a[n-1])!=1):
            ind=random.randint(0,14)
            a[0]=primes[ind]
            c+=1
        elif(a[n-1] not in primes and bltin_gcd(a[0],a[n-1])!=1):
            ind=random.randint(0,14)
            a[n-1]=primes[ind]
            c+=1       
    for i in range(1,n):
        if(bltin_gcd(a[i-1],a[i])!=1):
            if(a[i-1] not in primes and bltin_gcd(a[i-1],a[i])!=1):
                ind=random.randint(0,14)
                a[i-1]=primes[ind]
                c+=1
            elif(a[i] not in primes and bltin_gcd(a[i-1],a[i])!=1):
                ind=random.randint(0,14)
                a[i]=primes[ind]
                c+=1
    print(c)
    print(a)'''
                
                
            
            
    
    
