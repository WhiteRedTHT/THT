# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urun_sayisi_hata.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Depo_urun_yok_hata(object):
    def setupUi(self, Depo_urun_yok_hata):
        Depo_urun_yok_hata.setObjectName("Depo_urun_yok_hata")
        Depo_urun_yok_hata.resize(274, 98)
        Depo_urun_yok_hata.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Depo_urun_yok_hata)
        self.label.setGeometry(QtCore.QRect(10, 30, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")

        self.retranslateUi(Depo_urun_yok_hata)
        QtCore.QMetaObject.connectSlotsByName(Depo_urun_yok_hata)

    def retranslateUi(self, Depo_urun_yok_hata):
        _translate = QtCore.QCoreApplication.translate
        Depo_urun_yok_hata.setWindowTitle(_translate("Depo_urun_yok_hata", "Ürün Sayısı Hata"))
        self.label.setText(_translate("Depo_urun_yok_hata", "Depoda Girdiğiniz Değer Kadar Ürün Yok"))
