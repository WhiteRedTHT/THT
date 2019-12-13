# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hata_mesaj_depo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Hata(object):
    def setupUi(self, Hata):
        Hata.setObjectName("Hata")
        Hata.resize(268, 104)
        Hata.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Hata)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"")
        self.label.setObjectName("label")

        self.retranslateUi(Hata)
        QtCore.QMetaObject.connectSlotsByName(Hata)

    def retranslateUi(self, Hata):
        _translate = QtCore.QCoreApplication.translate
        Hata.setWindowTitle(_translate("Hata", "Depo Hata Mesaj"))
        self.label.setText(_translate("Hata", "Sadece Sayı Değeri Girebilirsiniz."))
