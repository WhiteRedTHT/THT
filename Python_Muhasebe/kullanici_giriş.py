import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.baglanti_olustur()

        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("database.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")
        self.baglanti.commit()

    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.kullanici_adi.setObjectName("kullanici_adi")
        self.user = QtWidgets.QLabel("AD   :")
        self.yazi_alani = QtWidgets.QLabel("")
        self.password = QtWidgets.QLabel("ŞİFRE :")
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.kaydol = QtWidgets.QPushButton("Kaydol")

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.user)
        h_box1.addWidget(self.kullanici_adi)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.password)
        h_box2.addWidget(self.parola)
        h_box2.addStretch()

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.yazi_alani)
        h_box3.addStretch()

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.giris)
        h_box4.addWidget(self.kaydol)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addStretch()
        v_box.addLayout(h_box4)

        self.user.setFixedSize(35, 20)
        self.password.setFixedSize(35, 20)
        self.kullanici_adi.setFixedSize(120, 20)
        self.parola.setFixedSize(120, 20)

        self.setLayout(v_box)

        self.giris.clicked.connect(self.login)
        self.kaydol.clicked.connect(self.kayit_ol)

        self.setStyleSheet("background-color:SandyBrown;")
        self.setGeometry(300, 100, 300, 300)
        self.setFixedSize(300, 300)
        self.setWindowTitle("KAYIT/GİRİŞ SİSTEMİ")

        self.show()

    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * From üyeler where kullanıcı_adı = ? and parola = ?", (adi, par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else:
            self.yazi_alani.setText("Hoş Geldiniz " + adi)
            pencere3.show()



    def kayit_ol(self):
        pencere2.show()


class pencere2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.arayuz()
        self.connect()

    def connect(self):
        self.baglanti2 = sqlite3.connect("database.db")
        self.cursor = self.baglanti2.cursor()
        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")
        self.baglanti2.commit()

    def arayuz(self):
        self.ad_label = QtWidgets.QLabel("AD   : ")
        self.sifre_label = QtWidgets.QLabel("ŞİFRE : ")
        self.ad_line = QtWidgets.QLineEdit()
        self.yazi_alani2 = QtWidgets.QLabel("")
        self.sifre_line = QtWidgets.QLineEdit()
        self.kaydet = QtWidgets.QPushButton("Kayıt Et")

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.ad_label)
        h_box1.addWidget(self.ad_line)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.sifre_label)
        h_box2.addWidget(self.sifre_line)
        h_box2.addStretch()

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.kaydet)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)

        self.setLayout(v_box)

        self.ad_label.setFixedSize(35, 20)
        self.ad_line.setFixedSize(120, 20)
        self.sifre_label.setFixedSize(35, 20)
        self.sifre_line.setFixedSize(120, 20)

        self.setWindowTitle("           KAYIT OL             ")
        self.setStyleSheet("background-color:SandyBrown")
        self.setFixedSize(300, 300)

        self.kaydet.clicked.connect(self.account)

    def account(self):
        adi2 = self.ad_line.text()
        sifre2 = self.sifre_line.text()



        self.cursor.execute("INSERT into üyeler Values(?,?)", (adi2, sifre2))
        self.baglanti2.commit()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    pencere = Pencere()
    pencere2 = pencere2()


    sys.exit(app.exec_())