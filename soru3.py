output = []
kelime = input("Kelimeyi gir: ")
alfabe = "abcdefghijklmnopqrstuvwxyz "

for harf in kelime:
    harf = harf.lower()  # Küçük harfe çevir, böylece büyük/küçük harf farklılığı olmaz
    if harf in alfabe:
        indeks = alfabe.index(harf)
        if harf == ' ':
            output.append(0)
        else:
            tekrar_sayisi = indeks % 3 + 1
            output.append([indeks // 3 + 2] * tekrar_sayisi)

print(output)
