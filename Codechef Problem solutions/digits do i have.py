n=int(input())
if(n>=0 and n<=9):
    print(1)
elif(n>=10 and n<=99):
    print(2)
elif(n>=100 and n<=999):
    print(3)
else:
    print("More than 3 digits")
