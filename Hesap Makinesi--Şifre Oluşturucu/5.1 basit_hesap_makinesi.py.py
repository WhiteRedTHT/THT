print("""©©©©©©©©©©©©©©©©©©©©©©©©
      
            ###########WhiteRed###########
            Hesap Makinesine Hoş Geldiniz!
            ###########WhiteRed###########

İşlemler;
1. Toplama işlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
Yukarıda ki işlemleri gerçekleştirebilirsiniz.
Programdan çıkmak için 'q'ya basınız.
©©©©©©©©©©©©©©©©©©©©©©©©""")

ilksayı = int(input("Birinci Sayıyı Giriniz:"))

ikincisayı = int(input("İkinci Sayıyı Giriniz:"))

while True:
    işlem = input("Seçmek istediğiniz işlemi yazınız:")
    
    if (işlem == "q"):
        print("Yine bekleriz...")
        break
    elif (işlem == "1"):
         print("{} ile {} in toplamı {} dır.".format(ilksayı,ikincisayı,ilksayı+ikincisayı))
         
    elif işlem == "2":
        print("{} ile {} in farkı {} dır.".format(ilksayı,ikincisayı,ilksayı-ikincisayı))  
        
    elif (işlem == "3"):
        print("{} ile {} in çarpımı {} dır.".format(ilksayı,ikincisayı,ilksayı * ikincisayı))
    
    elif işlem == "4":
        print("{} ile {} in bölümü {} dır.".format(ilksayı,ikincisayı,ilksayı / ikincisayı))
        continue
    else:
        print("Geçersiz İşlem")