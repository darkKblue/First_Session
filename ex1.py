num=int(input('num: '))
i=0
first=0
if 1<num<10**18:
    while num>0:
        first=num%10
        i=i+first
        num=num//10


    if i >= 10:
        ii=0
        add=i
        while add>0:
            z=add%10
            ii=ii+z
            add=add//10

        print(ii)
    else:
        print(i)
else:
    print("Error")

        
    
    

