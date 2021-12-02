i=input("Input : ")
print("Output :")

j=1
while j<=len(i):
    print(i[0:j])
    j+=1
for j in range(len(i),0,-1):
    print(i[0:j-1])
    j-=1