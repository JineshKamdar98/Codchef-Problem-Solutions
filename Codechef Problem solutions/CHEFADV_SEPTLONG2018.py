# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:39:45 2018

@author: Jasmin
"""

for _ in range(int(input())):
    n,m,x,y = map(int,input().split())
    k=1
    p=1
    rem_k = n%x
    rem_p = m%y
    if(n==x and rem_p==0) or (rem_k==0 and m==y) or (n==x and m==y) or (rem_k==2 and rem_p==2) or (rem_k==1 and rem_p==1):
        print("Chefirnemo")
    else:
        print("Pofik")