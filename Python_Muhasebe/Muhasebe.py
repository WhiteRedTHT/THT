from PyQt5 import QtWidgets
import sys
import sqlite3
from muhasebe_goruntu import Ui_Muhasebe
from giris_yap import Ui_Giris_yap
from kayit_ol import Ui_kayit_ol
from hata import Ui_Hata
from hata_urun_sayi import Ui_Depo_urun_yok_hata
from musteri_yok import Ui_Musteri_yok_Hata
import time


class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()

        self.ui = Ui_Muhasebe()
        self.ui.setupUi(self)
        self.baglanti()
        self.urunler()
        self.ui.depodaki_urunler_goster_buton.clicked.connect(self.depo_urunler_tablo)
        self.ui.Urun_fiyatlari_buton_goster.clicked.connect(self.depo_urun_fiyat)
        self.ui.musteriler_buton_goster.clicked.connect(self.musteriler)
        self.ui.musteri_kayit_buton.clicked.connect(self.musteri_kayit)
        self.ui.siparis_ver_buton.clicked.connect(self.siparis_verme)



    def baglanti(self):
        self.baglanti = sqlite3.connect("muhasebe.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS urunler (urun_adi TEXT, urun_adedi INT, urun_fiyat INT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS musteriler (musteri_adi TEXT, musteri_soyad TEXT)")
        self.baglanti.commit()

    def urunler(self):
        self.cursor.execute("INSERT INTO  urunler VALUES('Dizüstü',1000,3500)")
        self.cursor.execute("INSERT INTO  urunler VALUES('Masaüstü',200,10000)")
        self.cursor.execute("INSERT INTO  urunler VALUES('TV',3000,5000)")
        self.cursor.execute("INSERT INTO  urunler VALUES('Kulaklık',7000,700)")
        self.cursor.execute("INSERT INTO  urunler VALUES('Drone',250,6000)")
        self.cursor.execute("INSERT INTO  urunler VALUES('Telefon',100,2000)")
        self.baglanti.commit()

    def depo_urunler_tablo(self):

        self.cursor.execute("Select urun_adedi From urunler")
        self.liste = self.cursor.fetchall()
        deneme = []
        for i in self.liste:
            deneme.append(i)

        self.ui.depo_dizustu_text_edit.setText(str(deneme[0][0]))
        self.ui.depo_masaustu_text_edit.setText(str(deneme[1][0]))
        self.ui.depo_tv_text_edit.setText(str(deneme[2][0]))
        self.ui.depo_kulaklik_text_edit.setText(str(deneme[3][0]))
        self.ui.depo_drone_text_edit.setText(str(deneme[4][0]))
        self.ui.depo_telefon_text_edit.setText(str(deneme[5][0]))





    def depo_urun_fiyat(self):
        self.cursor.execute("Select urun_fiyat From urunler")
        self.liste2 = self.cursor.fetchall()
        deneme = []
        for a in self.liste2:
            deneme.append(a)
        self.ui.fiyat_dizustu_text_edit.setText(str(deneme[0][0]))
        self.ui.fiyat_masaustu_text_edit.setText(str(deneme[1][0]))
        self.ui.fiyat_tv_text_edit.setText(str(deneme[2][0]))
        self.ui.fiyat_kulaklik_text_edit.setText(str(deneme[3][0]))
        self.ui.fiyat_drone_text_edit.setText(str(deneme[4][0]))
        self.ui.fiyat_telefon_text_edit.setText(str(deneme[5][0]))

    def musteriler(self):
        self.cursor.execute("Select musteri_adi From musteriler")
        self.list3 = self.cursor.fetchall()
        self.cursor.execute("Select musteri_soyad From musteriler")
        self.list4 = self.cursor.fetchall()
        datadan_veri2 = []
        liste_donusturme2 = []
        datadan_veri = []
        liste_donusturme = []


        for a in self.list3:
            datadan_veri.append(a)

        for b in self.list4:
            datadan_veri2.append(b)

        if len(datadan_veri) != 0:
            for c in datadan_veri:
                liste_donusturme.append(c[0])

            for d in datadan_veri2:
                liste_donusturme2.append(d[0])


            for e in range(0,len(liste_donusturme2)):
                self.ui.musteriler_soyad_text_edit.append(str(liste_donusturme2[e]))

            for i in range(0, len(liste_donusturme)):
                self.ui.musteriler_isim_text_edit.append(str(liste_donusturme[i]))
        else:
            Musteri_sayi_yok.show()




    def musteri_kayit(self): #Müşsteri ekle sekmesinde ki verileri database'e aktarmaktadır.
        musteri_adi = self.ui.isim_kayit_line.text()
        musteri_soyad = self.ui.soyisim_kayit_line.text()
        if musteri_soyad == "" or musteri_adi == "":
            self.ui.kayt_durum_label.setText("Kayıt Başarısız")
        else:
            self.cursor.execute("INSERT INTO musteriler VALUES(?,?)", (musteri_adi, musteri_soyad))
            self.ui.kayt_durum_label.setText("Kayıt Başarılı")
            self.baglanti.commit()
            self.ui.musteriler_isim_text_edit.setText("") #Müşteriler kısmında bunu yapmazsak Göster butonuna tıklayınca 2 kere listeyi gösteriyor.
            self.ui.musteriler_soyad_text_edit.setText("")


    def siparis_verme(self):
        try:
            self.urun_ismi = self.ui.urun_isim_siparis_line.text()
            urun_adedi = self.ui.urun_miktar_siparis_line.text()
            self.cursor.execute("SELECT * FROM urunler WHERE urun_adi = ? ", (self.urun_ismi,))
            self.liste = self.cursor.fetchall()

            veriler = []
            veriler2 = []

            for i in self.liste: #Database'den aldığı değerleri veriler listesine aktaracak
                veriler.append(i)

            for b in veriler: #veriler2 listesine veriler listesinin 1. indeksini atacak
                veriler2.append(b[1])

            alinan_veri = veriler2[0]

            self.deneme = int(alinan_veri)-int(urun_adedi) #kullanıcıdan aldığı sayı değerini database'de ki veriden çıkaracak
            if self.deneme >= 0:
                self.cursor.execute("Update urunler SET urun_adedi=? where urun_adi=?",(self.deneme,self.urun_ismi)) #kullanıcıdan aldığı veriyi database de ki veriden çıkarttıktan sonra yeni oluşan sayıyı database'e aktaracak
                self.baglanti.commit()
                self.ui.siparis_durum.setText(f"İstediğiniz {self.urun_ismi} üründen {urun_adedi} adet \nsipariş alındı.")
            else:
                Depo_urun_sayisi_hata.show()

        except:
            Depo_urun_hata.show()



class Giris_Yap(QtWidgets.QWidget):
    def __init__(self):
        super(Giris_Yap, self).__init__()
        self.ab = Ui_Giris_yap()
        self.ab.setupUi(self)
        self.connect2()
        self.ab.kayit_ol_buton.clicked.connect(self.kayit) #giriş yap ksımında ki kayit ol butonuna tıklarsak kayit ol kısmına yönlendirecek
        self.ab.giris_yap_buton.clicked.connect(self.login) #giriş yap kısmında ki giriş yap kısmına tıklarsak giriş yaptıracak veya hata mesajı dönecek

    def connect2(self): #Database ile bağlantı kuracak
        self.baglanti = sqlite3.connect("muhasebe.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler (kullanici_adi TEXT, parola TEXT)")
        self.baglanti.commit()


    def login(self): #Giriş yapmak için
        adi = self.ab.kullanici_adi_line.text()
        par = self.ab.sifre_line.text()


        self.cursor.execute("Select * From uyeler where kullanici_adi = ? and parola = ?", (adi, par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.ab.durum_giris_ekran_label.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else:
            self.ab.durum_giris_ekran_label.setText("Hoş Geldiniz " + adi)
            time.sleep(1)

            self.muhasebe()


    def kayit(self):
        Kayit_Ol.show() #kayıt ol sekmesini açacak
    def muhasebe(self):
        Muhasebe.show() #muhasebe uygulamasını açacak

class Kayit_Ol(QtWidgets.QWidget):
    def __init__(self):
        super(Kayit_Ol, self).__init__()
        self.ac = Ui_kayit_ol()
        self.ac.setupUi(self)
        self.ac.kayit_ol_buton.clicked.connect(self.account)
        self.connect()


    def connect(self): #Database ile bağlantı kuracak
        self.baglanti = sqlite3.connect("muhasebe.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler(kullanici_adi TEXT, parola TEXT)")
        self.baglanti.commit()

    def account(self): #Database'e kayit ol sekmesinde ki verileri yazdıracak
        adi2 = self.ac.kayit_kullanici_adi_line.text()
        sifre2 = self.ac.kayit_sifre_line.text()
        self.cursor.execute("INSERT into uyeler Values(?,?)", (adi2, sifre2))
        self.baglanti.commit()
        self.ac.kayit_ol_durum.setText("Başarıyla Kayıt Oldunuz " + adi2)


class Depo_sayi_urun_hata(QtWidgets.QWidget): #Ürün sipariş verme kısmında str değer girerse açılacak.
    def __init__(self):
        super(Depo_sayi_urun_hata, self).__init__()
        self.ad = Ui_Hata()
        self.ad.setupUi(self)

class Depo_Urun_Sayısı_Hata(QtWidgets.QWidget):
    def __init__(self):
        super(Depo_Urun_Sayısı_Hata, self).__init__()
        self.ad = Ui_Depo_urun_yok_hata()
        self.ad.setupUi(self)

class Musteri_Sayi_Yok(QtWidgets.QWidget):
    def __init__(self):
        super(Musteri_Sayi_Yok, self).__init__()
        self.af = Ui_Musteri_yok_Hata()
        self.af.setupUi(self)









app = QtWidgets.QApplication(sys.argv)
Muhasebe = App()
Giris_Yap = Giris_Yap()
Kayit_Ol = Kayit_Ol()
Depo_urun_hata = Depo_sayi_urun_hata()
Depo_urun_sayisi_hata = Depo_Urun_Sayısı_Hata()
Musteri_sayi_yok = Musteri_Sayi_Yok()
Giris_Yap.show()

sys.exit(app.exec_())

