n=int(input(': '))
i=int(input(': '))
j=int(input(': '))

c=int()
b=int()


if n%i==0:
    print(n,(n//i),0)
elif n%j==0:
    print(n,0,(n//j))
elif not (n%i==0 and n%j==0):
    c=n%i
    result=c%j
    b = n % j
    second_res = b % i
    if result==0:

        print(n,n//i,c//j)
       
    elif second_res==0:
        print(n, b // i, n // j)

    elif c%j==c or n%j==n:
            print("-1")



