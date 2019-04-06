from fractions import Fraction
s=input()
a=s.split(" ")
print(a)
t=int(a[0])
for i in range(t):
    x=int(a[i+1])
    if(x%2==0):
        s1=str(Fraction((2**x)-1,3*(2**x)))
        h=s1.index('/')
        print(s1[0:h],s1[h+1:],end=" ")
    else:
        s2=str(Fraction((2**x)+1,3*(2**x)))
        f=s2.index('/')
        print(s2[0:f],s2[f+1:],end=" ")
