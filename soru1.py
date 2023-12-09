# soru 1;
sayilar=[]
sayac=0
denek=0
while True:
    sayi=int(input("sayıları gir :"))
    sayac+=1
    sayilar.append(sayi)
    secenek=input("devamsa:devam | tamamsa:tamam girin.")
    if secenek=="tamam":
        break
hedef=int(input("hedef sayıyı seç:"))
for i in range(sayac):
    for j in range(sayac):
        if sayilar[i]+sayilar[j]==hedef:
            indis1=sayilar.index(sayilar[i])
            indis2=sayilar.index(sayilar[j])
            denek+=1
            break
    if denek==1:
        break
print("girilen sayılar =",sayilar)
print("hedef =",hedef)
if denek==1:
    print("hedefi sağlayan sayıların indisleri = (",indis1,",",indis2,")")
if denek==0:
    print("sayıların toplamı hedefe ulaşmıyor.")
