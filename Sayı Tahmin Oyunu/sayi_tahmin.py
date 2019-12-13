import random
print("""**************************************
Sayı Tahmin Uygulamasına Hoş Geldiniz!


**************************************
""")

sayi_rastgele = random.randint(1,100)

tahmin = 0
while True:
    sayi = input("1 ile 100 arasında bir sayı giriniz.(Programdan çıkmak için 'q' harfine basınız.): ")
    tahmin +=1
    if sayi== "q":
        print("Programdan çıkış yapılıyor, tekrar görüşmek üzere...")
        break
    elif int(sayi) < sayi_rastgele:
        print("\nYazmış olduğunuz sayı, sistemde ki sayıdan küçüktür. Biraz daha büyültün :)\n ")
        continue
    elif int(sayi) > sayi_rastgele:
        print("\nYazmış olduğunuz sayı, sistemde ki sayıdan büyüktür. Biraz daha küçültün :)\n")
        continue
    else:
        print("\nTebrikler sayıyı buldunuz! Sayımız: {} Deneme Sayısı: {}".format(sayi_rastgele,tahmin))
        input()
        break

