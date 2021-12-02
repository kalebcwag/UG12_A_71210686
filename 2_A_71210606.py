totnama=[]
totkursi=[]

n=0
while n==0:
    nama=str(input("Masukkan nama : "))
    if nama!="STOP":
        kursi=int(input("Masukkan nomor kursi : "))
        if kursi not in totkursi:
            totnama.append(nama)
            totkursi.append(kursi)
        else:
            print("Mohon maaf kursi tersebut telah terisi!")
    else:
        break

print("")
for i in range(len(totnama)):
    print("Kursi nomor {} telah diisi oleh {}".format(totkursi[i],totnama[i]))