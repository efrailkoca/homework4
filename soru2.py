# soru 2;
sifirDizileri=[]
enAz=0
sayilar=[]
sayac=0
denek=0
for i in range(3000):
    sayi=int(input("sayıları girin :"))
    sayac+=1
    sayilar.append(sayi)
    enAz+=1
    secenek=input("devamsa:devam | tamamsa:tamam girin.")
    if secenek=="tamam" and enAz>=3:
        break
for i in range(sayac):
    for j in range(sayac):
        for k in range(sayac):
            if i==j:
                break
            for a in range(1):
                if i==k or j==k:
                    break
                elif sayilar[i]+sayilar[j]+sayilar[k]==0:
                    dizi=[sayilar[i],sayilar[j],sayilar[k]]
                    if dizi not in sifirDizileri:
                        sifirDizileri.append(dizi)
                        denek+=1
print("girilen sayılar =",sayilar)
if denek!=0:
    print("sıfır yapan diziler =",sifirDizileri)
else:
    print("sayıların toplamı sıfır yapan bir üçlü yok.")
