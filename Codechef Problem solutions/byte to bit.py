for t in range(int(input())):
    n=int(input())
    n=n-1
    bit,nibble,byte=0,0,0
    r=n%26
    k=n//26
    if(r>=0 and r<2):
        bit+=pow(2,k)
        print(bit,nibble,byte)
    elif(r>=2 and r<10):
        nibble+=pow(2,k)
        print(bit,nibble,byte)
    elif(r>=10 and r<26):
        byte+=pow(2,k)
        print(bit,nibble,byte)
        

            
            
        
