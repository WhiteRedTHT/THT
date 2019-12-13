import random
import string

print("""•••••••••••••••••••••••••••••••••••••••••••••••••••
      ###########WhiteRed###########
      Parola Oluşturucuya Hoş Geldiniz!
      ###########WhiteRed#############
Parolanızı oluşturmak için aşağıda verilen soruları isteğinize göre doldurunuz ve "Enter" tuşuna basınız.

    
NOT: Programdan çıkmak için "q" tuşuna basınız. 
•••••••••••••••••••••••••••••••••••••••••••••••••••""")

harfler = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sayilar = '0123456789'
karakterler = "'"'"'"!#@.,$"

while True:
    soru_sayi = input("Parolanın içerisinde sayı olsun mu? [E/H]: ")
    if soru_sayi != 'E' and soru_sayi != 'H':
        print('Hatalı giriş - E veya H girin')
        continue
    
    while True:
        soru_harf = input("Parolanızda harf olsun mu? [E/H]: ")
        if soru_harf != 'E' and soru_harf != 'H':
            print('Hatalı giriş - E veya H girin')
            continue
        
        while True:
            soru_karakter = input("Parolanın içerisinde özel karakter olsun mu? [E/H]: ")
            if soru_karakter != "E" and soru_karakter != "H" :
                print("Hatalı giriş -E veya H girin")
                continue
        
            while True:
                soru_min = int(input("Parolanız minumum kaç karakter olsun? "))
                soru_maks = int(input("Parolanız maksimum kaç karakter olsun? "))
                if soru_min <= 0 and soru_min >= soru_maks:
                    print("Lütfen geçerli değerleri giriniz.")
                    
                    
                    continue
                break
            break
        break
    break

def rastgeleseçenek(stringLength = soru_min):
        if soru_sayi == "E" and soru_harf == "H" and soru_karakter == "E" :
            şifrekarakterleri = karakterler + sayilar  
        elif soru_sayi == "E" and soru_harf == "E" and soru_karakter == "H" :
            şifrekarakterleri = sayilar + harfler 
        elif soru_sayi == "H" and soru_harf == "E" and soru_karakter == "E" :
            şifrekarakterleri = karakterler + harfler 
        elif soru_sayi == "E" and soru_harf == "H" and soru_karakter == "H" :
            şifrekarakterleri = sayilar 
        elif soru_sayi == "H" and soru_harf == "E" and soru_karakter == "H" :
            şifrekarakterleri = harfler 
        elif soru_sayi == "H" and soru_harf == "H" and soru_karakter == "E" :
            şifrekarakterleri = karakterler
        elif soru_sayi == "E" and soru_harf == "E" and soru_karakter == "E" :
            şifrekarakterleri = karakterler + sayilar + harfler 
        return ''.join(random.choice(şifrekarakterleri) for i in range(stringLength))
print ("Şifre", rastgeleseçenek(soru_min) )
    
while True:
   a = input("Programdan çıkmak için 'q' ya basınız  ")
   if a == "q" :
        print("Programdan çıkıyorsunuz....")
        break
    