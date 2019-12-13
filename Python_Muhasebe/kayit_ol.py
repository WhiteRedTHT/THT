# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit_ol.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kayit_ol(object):
    def setupUi(self, kayit_ol):
        kayit_ol.setObjectName("kayit_ol")
        kayit_ol.resize(371, 209)
        kayit_ol.setStyleSheet("background-color: rgb(16, 170, 165);")
        self.kayit_kullanici_adi_label = QtWidgets.QLabel(kayit_ol)
        self.kayit_kullanici_adi_label.setGeometry(QtCore.QRect(60, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kayit_kullanici_adi_label.setFont(font)
        self.kayit_kullanici_adi_label.setObjectName("kayit_kullanici_adi_label")
        self.kayt_sifre_label = QtWidgets.QLabel(kayit_ol)
        self.kayt_sifre_label.setGeometry(QtCore.QRect(100, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kayt_sifre_label.setFont(font)
        self.kayt_sifre_label.setObjectName("kayt_sifre_label")
        self.kayit_kullanici_adi_line = QtWidgets.QLineEdit(kayit_ol)
        self.kayit_kullanici_adi_line.setGeometry(QtCore.QRect(160, 50, 113, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kayit_kullanici_adi_line.setFont(font)
        self.kayit_kullanici_adi_line.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.kayit_kullanici_adi_line.setObjectName("kayit_kullanici_adi_line")
        self.kayit_sifre_line = QtWidgets.QLineEdit(kayit_ol)
        self.kayit_sifre_line.setGeometry(QtCore.QRect(160, 80, 113, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kayit_sifre_line.setFont(font)
        self.kayit_sifre_line.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.kayit_sifre_line.setObjectName("kayit_sifre_line")
        self.kayit_ol_buton = QtWidgets.QPushButton(kayit_ol)
        self.kayit_ol_buton.setGeometry(QtCore.QRect(140, 120, 75, 23))
        self.kayit_ol_buton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.kayit_ol_buton.setObjectName("kayit_ol_buton")
        self.durum_label = QtWidgets.QLabel(kayit_ol)
        self.durum_label.setGeometry(QtCore.QRect(120, 160, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.durum_label.setFont(font)
        self.durum_label.setText("")
        self.durum_label.setObjectName("durum_label")
        self.kayit_ol_durum = QtWidgets.QLabel(kayit_ol)
        self.kayit_ol_durum.setGeometry(QtCore.QRect(100, 150, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.kayit_ol_durum.setFont(font)
        self.kayit_ol_durum.setText("")
        self.kayit_ol_durum.setObjectName("kayit_ol_durum")

        self.retranslateUi(kayit_ol)
        QtCore.QMetaObject.connectSlotsByName(kayit_ol)

    def retranslateUi(self, kayit_ol):
        _translate = QtCore.QCoreApplication.translate
        kayit_ol.setWindowTitle(_translate("kayit_ol", "Kayıt Ol Ekranı"))
        self.kayit_kullanici_adi_label.setText(_translate("kayit_ol", "Kullanıcı Adı :"))
        self.kayt_sifre_label.setText(_translate("kayit_ol", "Şifre :"))
        self.kayit_ol_buton.setText(_translate("kayit_ol", "Kayıt Ol"))
