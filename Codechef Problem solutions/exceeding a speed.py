s=int(input())
f=0
if(s<=90):
    f=0
    print(str(f)+' '+'No punishment')
elif(s>=91 and s<=110):
    f=int((s-90)*300)
    print(str(f)+' '+'Warning')
elif(s>110):
    f=int((s-90)*500)
    print(str(f)+' '+'License removed')

