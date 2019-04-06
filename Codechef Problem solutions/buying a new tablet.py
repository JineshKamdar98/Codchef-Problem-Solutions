for t in range(int(input())):
    n,b=map(int,input().split())
    l=[]
    for i in range(n):
        w,h,p=input().split()
        w,h,p=[int(w),int(h),int(p)]
        if(p<=b):
            l.append(w*h)
    if(l!=[]):
        print(max(l))
    else:
        print("no tablet")
        
            
