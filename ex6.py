Result=list()

a=1
b=a+1

num=int(input())
while a<num:
    R = -1

    m=a
    n=b
    print('-------')
    print('a :',a)
    print('b :',b)
    print('m :',m)
    print('n :',n)
    print('R :',R)
    print('-------')
    while R != 0:
        R = m % n
        if R == 0:
            break
        m = n
        n = R
    Result.append(n)

    print('Result = ',Result)

    if b==num:
        a+=1
        b=a+1

    else:
        b+=1
    print('******')
    print('a :', a)
    print('b :', b)
    print('m :', m)
    print('n :', n)
    print('R :', R)
    print('******')


print(Result)
print(max(Result))







