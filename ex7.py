num=int(input())
count=0
x=0
for i in range(1,num+1):
    for j in range(1,i+1):
        if i%j==0:
            x=x+j
            count+=1
print(count,x)