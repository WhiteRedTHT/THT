# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris_yap.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Giris_yap(object):
    def setupUi(self, Giris_yap):
        Giris_yap.setObjectName("Giris_yap")
        Giris_yap.resize(371, 209)
        Giris_yap.setStyleSheet("background-color: rgb(16, 170, 165);")
        self.kullanici_adi_label = QtWidgets.QLabel(Giris_yap)
        self.kullanici_adi_label.setGeometry(QtCore.QRect(60, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kullanici_adi_label.setFont(font)
        self.kullanici_adi_label.setObjectName("kullanici_adi_label")
        self.sifre_label = QtWidgets.QLabel(Giris_yap)
        self.sifre_label.setGeometry(QtCore.QRect(100, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sifre_label.setFont(font)
        self.sifre_label.setObjectName("sifre_label")
        self.kullanici_adi_line = QtWidgets.QLineEdit(Giris_yap)
        self.kullanici_adi_line.setGeometry(QtCore.QRect(160, 50, 113, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kullanici_adi_line.setFont(font)
        self.kullanici_adi_line.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.kullanici_adi_line.setText("")
        self.kullanici_adi_line.setObjectName("kullanici_adi_line")
        self.sifre_line = QtWidgets.QLineEdit(Giris_yap)
        self.sifre_line.setGeometry(QtCore.QRect(160, 80, 113, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sifre_line.setFont(font)
        self.sifre_line.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.sifre_line.setObjectName("sifre_line")
        self.giris_yap_buton = QtWidgets.QPushButton(Giris_yap)
        self.giris_yap_buton.setGeometry(QtCore.QRect(190, 120, 75, 23))
        self.giris_yap_buton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.giris_yap_buton.setObjectName("giris_yap_buton")
        self.kayit_ol_buton = QtWidgets.QPushButton(Giris_yap)
        self.kayit_ol_buton.setGeometry(QtCore.QRect(80, 120, 75, 23))
        self.kayit_ol_buton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.kayit_ol_buton.setObjectName("kayit_ol_buton")
        self.durum_giris_ekran_label = QtWidgets.QLabel(Giris_yap)
        self.durum_giris_ekran_label.setGeometry(QtCore.QRect(110, 160, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.durum_giris_ekran_label.setFont(font)
        self.durum_giris_ekran_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.durum_giris_ekran_label.setText("")
        self.durum_giris_ekran_label.setObjectName("durum_giris_ekran_label")

        self.retranslateUi(Giris_yap)
        QtCore.QMetaObject.connectSlotsByName(Giris_yap)

    def retranslateUi(self, Giris_yap):
        _translate = QtCore.QCoreApplication.translate
        Giris_yap.setWindowTitle(_translate("Giris_yap", "Giriş Ekranı"))
        self.kullanici_adi_label.setText(_translate("Giris_yap", "Kullanıcı Adı :"))
        self.sifre_label.setText(_translate("Giris_yap", "Şifre :"))
        self.giris_yap_buton.setText(_translate("Giris_yap", "Giriş Yap"))
        self.kayit_ol_buton.setText(_translate("Giris_yap", "Kayıt Ol"))
