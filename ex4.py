First_input=int(input("Enter Number of Numbers : "))
Number_list=list()
counter=0
for i in range(First_input):
    x=int(input())
    Number_list.append(x)
#print(Number_list)
for index in Number_list:
    for j in range(1,index+1):
        #print('j = ',j)
        #print('index = ',index)
        baghimandeh=index%j
        #print('baghimandeh =',baghimandeh)

        if baghimandeh==0:
            counter+=1
            #print('counter = ',counter)
            #print('/////////////')
        
    if counter==3:
        Yes_value=print('yes')
        #print('-------------')
        counter=0

    else:
        No_value=print('No')
        #print('-------------')
        counter=0

    