#ödevler --- ilk değerler kullanıcıdan alınacak
# girilen sayının pozitif, negatif veya sıfır olduğunu yazan koşul
# girilen sayının tek mi çift mi olduğunu yazan koşul
# Girilen nota göre harf aralığını yazan koşul (80-100 A, 60-80 B vs.)
# girilen ismin karakter sayısı 5den büyükse "uzun bir isminiz var" değilse ismini yazsın
#girilen sayının asal olup olmadığını bulan kod dizisi. (for ve while)
# notlar=[45,85,75,50] içinde 75 değerinin indisini yazdıran döngü
# girilen sayının faktöriyelini bulma(for ve while ile)
#kullanıcıdan pozitif bir sayı bekleyen pozitifi gördüğü an bastıran negatif sayı girildikçe bir daha soran for döngüsü

# girilen sayının pozitif, negatif veya sıfır olduğunu yazan koşul
sayi=int(input("sayiyi giriniz:"))
if sayi<0:
    print("negatif sayi girdiniz")
elif sayi==0:
    print("0 girdiniz")
else:
    print("pozitif sayi girdiniz")

# girilen sayının tek mi çift mi olduğunu yazan koşul
if sayi%2==1:
    print("tek sayi girdiniz")
else:
    print("cift sayi girdiniz")

#girilen sayının asal olup olmadığını bulan kod dizisi. while ile
sayim=int(input("(while)asal mı kontrel edeceğiniz sayiyi giriniz:"))
if sayim>0:
    i=2
    countt=0
    while i< sayim:
        if sayim%i==0:
            countt=countt+1
            break
        i+=1
    if countt>0:
        print("sayi asal değil")
    else:
        print("sayi asaldir")
else:
    print("asal sayı kontrolü için 1den büyük sayi giriniz")


#girilen sayının asal olup olmadığını bulan kod dizisi. for ile
sayim=int(input("(for)asal mı kontrel edeceğiniz sayiyi giriniz:"))
if sayim>0:
    i=2
    countt=0
    for i in range(2, sayi):
        if sayim%i==0:
            countt=countt+1
            
    if countt>0:
        print("sayi asal değil")
    else:
        print("sayi asaldir")
else:
    print("asal sayı kontrolü için 1den büyük sayi giriniz")



# Girilen nota göre harf aralığını yazan koşul (80-100 A, 60-80 B vs.)
nott=float(input("notunuzu giriniz:"))
if 80 <= nott <= 100:
    print("Harf Notu: A")
elif 60 <= nott < 80:
    print("Harf Notu: B")
elif 40 <= nott < 60:
    print("Harf Notu: C")
elif 20 <= nott < 40:
    print("Harf Notu: D")
elif 0 <= nott < 20:
    print("Harf Notu: F")
else:
    print("Geçersiz not! Lütfen 0 ile 100 arasında bir değer girin.")

# girilen ismin karakter sayısı 5den büyükse "uzun bir isminiz var" değilse ismini yazsın
isim=input("isminizi giriniz:")
uzunluk=len(isim)
if uzunluk<=5:
    print(isim)
else:
    print("uzun bir isminiz var")


# notlar=[45,85,75,50] içinde 75 değerinin indisini yazdıran döngü
notlar=[45,85,75,50]
for i in range (len(notlar)):
    if notlar[i]==75:
        print("75e ulaştın")


# girilen sayının faktöriyelini bulma for ile
sayi=int(input("(for)faktoriyel hesabi için sayiyi giriniz:"))
if(sayi<0):
    print("sayiyi 0dan büyük girin")
carpim=1
for i in range(1,sayi+1):
    carpim=carpim*i
print(carpim)


# girilen sayının faktöriyelini bulma while ile
sayi=int(input("(while)faktoriyel hesabi için sayiyi giriniz:"))
if(sayi<0):
    print("sayiyi 0dan büyük girin")
carpim=1
i=1
while i<sayi+1:
    carpim=carpim*i
    i+=1
print(carpim)


#kullanıcıdan pozitif bir sayı bekleyen pozitifi gördüğü an bastıran negatif sayı girildikçe bir daha soran for döngüsü
for _ in range(100):
    sayi=int(input("(cikmak icin f tuşuna basın)sayinizi girin:"))
    string_sayi = str(sayi)
    if string_sayi.lower() == 'f':  # 'f' tuşuna basıldığında çıkmak
        print("Çıkılıyor...")
        break
    try:
        if sayi>=0:
            print(sayi)
            
        else:
            continue
    except ValueError:
        print("gecersiz giris")
