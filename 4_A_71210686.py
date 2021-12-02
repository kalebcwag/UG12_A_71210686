jumlah=int(input("Input : "))
count=0
for i in range(1,jumlah) : 
    for j in range(i,jumlah) :
        print(' ',end='')
    while (count!=(2*i-1)):
        if (count==0 or count==2*i-2) :
            print("*",end="")
        else :
            print(" ",end ="")
        count+=1
    count=0
    print("")
for i in range(0,jumlah) :
    print("*",end=" ")