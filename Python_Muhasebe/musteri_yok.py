# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musteri_yok_hata.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Musteri_yok_Hata(object):
    def setupUi(self, Musteri_yok_Hata):
        Musteri_yok_Hata.setObjectName("Musteri_yok_Hata")
        Musteri_yok_Hata.resize(349, 103)
        Musteri_yok_Hata.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.musteri_hata = QtWidgets.QLabel(Musteri_yok_Hata)
        self.musteri_hata.setGeometry(QtCore.QRect(50, 20, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.musteri_hata.setFont(font)
        self.musteri_hata.setStyleSheet("color: rgb(255, 0, 0);\n"
"")
        self.musteri_hata.setObjectName("musteri_hata")

        self.retranslateUi(Musteri_yok_Hata)
        QtCore.QMetaObject.connectSlotsByName(Musteri_yok_Hata)

    def retranslateUi(self, Musteri_yok_Hata):
        _translate = QtCore.QCoreApplication.translate
        Musteri_yok_Hata.setWindowTitle(_translate("Musteri_yok_Hata", "Müşteri Yok Hata"))
        self.musteri_hata.setText(_translate("Musteri_yok_Hata", "Hiç müşteriniz yok, müşteri eklemelisiniz."))
