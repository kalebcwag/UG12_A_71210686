n=input("Masukkan deret angka: ")

n=n.split(",")
angka=[]

for i in n:
    i=int(i)
    if i%2==0:
        angka.append(i)
    else:
        angka.append(i*-1)

print("Total :",end="")
for i in range(len(angka)):
    if angka[i]%2==0:
        print("+",angka[i],end=" ")
    else:
        print(angka[i],end=" ")
print()
print("Hasil perhitungan diatas ialah",sum(angka))