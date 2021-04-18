n=int(input())
k=int(input())
even=list()
odd=list()
for index in range(1,n+1):
    if index%2==0:
        even.append(index)
    else:
        odd.append(index)
even.reverse()
odd.extend(even)
print(odd)
print(odd[k-1])

