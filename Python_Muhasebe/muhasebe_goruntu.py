# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'muhasebe.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Muhasebe(object):
    def setupUi(self, Muhasebe):
        Muhasebe.setObjectName("Muhasebe")
        Muhasebe.resize(640, 271)
        self.muhasebe = QtWidgets.QTabWidget(Muhasebe)
        self.muhasebe.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.muhasebe.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"")
        self.muhasebe.setObjectName("muhasebe")
        self.Depo_urunler_Tab = QtWidgets.QWidget()
        self.Depo_urunler_Tab.setObjectName("Depo_urunler_Tab")
        self.Depoda_ki_urunler_baslik = QtWidgets.QLabel(self.Depo_urunler_Tab)
        self.Depoda_ki_urunler_baslik.setGeometry(QtCore.QRect(210, 40, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Depoda_ki_urunler_baslik.setFont(font)
        self.Depoda_ki_urunler_baslik.setObjectName("Depoda_ki_urunler_baslik")
        self.dizustu_label = QtWidgets.QLabel(self.Depo_urunler_Tab)
        self.dizustu_label.setGeometry(QtCore.QRect(30, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dizustu_label.setFont(font)
        self.dizustu_label.setObjectName("dizustu_label")
        self.masaustu_label = QtWidgets.QLabel(self.Depo_urunler_Tab)
        self.masaustu_label.setGeometry(QtCore.QRect(30, 140, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.masaustu_label.setFont(font)
        self.masaustu_label.setObjectName("masaustu_label")
        self.TV_label = QtWidgets.QLabel(self.Depo_urunler_Tab)
        self.TV_label.setGeometry(QtCore.QRect(30, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TV_label.setFont(font)
        self.TV_label.setObjectName("TV_label")
        self.kulaklik_label = QtWidgets.QLabel(self.Depo_urunler_Tab)
        self.kulaklik_label.setGeometry(QtCore.QRect(330, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kulaklik_label.setFont(font)
        self.kulaklik_label.setObjectName("kulaklik_label")
        self.drone_label = QtWidgets.QLabel(self.Depo_urunler_Tab)
        self.drone_label.setGeometry(QtCore.QRect(330, 140, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.drone_label.setFont(font)
        self.drone_label.setObjectName("drone_label")
        self.telefon_label = QtWidgets.QLabel(self.Depo_urunler_Tab)
        self.telefon_label.setGeometry(QtCore.QRect(330, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.telefon_label.setFont(font)
        self.telefon_label.setObjectName("telefon_label")
        self.depodaki_urunler_goster_buton = QtWidgets.QPushButton(self.Depo_urunler_Tab)
        self.depodaki_urunler_goster_buton.setGeometry(QtCore.QRect(250, 210, 75, 23))
        self.depodaki_urunler_goster_buton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.depodaki_urunler_goster_buton.setObjectName("depodaki_urunler_goster_buton")
        self.depo_dizustu_text_edit = QtWidgets.QTextEdit(self.Depo_urunler_Tab)
        self.depo_dizustu_text_edit.setGeometry(QtCore.QRect(110, 110, 104, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.depo_dizustu_text_edit.setFont(font)
        self.depo_dizustu_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.depo_dizustu_text_edit.setObjectName("depo_dizustu_text_edit")
        self.depo_masaustu_text_edit = QtWidgets.QTextEdit(self.Depo_urunler_Tab)
        self.depo_masaustu_text_edit.setGeometry(QtCore.QRect(110, 140, 104, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.depo_masaustu_text_edit.setFont(font)
        self.depo_masaustu_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.depo_masaustu_text_edit.setObjectName("depo_masaustu_text_edit")
        self.depo_tv_text_edit = QtWidgets.QTextEdit(self.Depo_urunler_Tab)
        self.depo_tv_text_edit.setGeometry(QtCore.QRect(110, 170, 104, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.depo_tv_text_edit.setFont(font)
        self.depo_tv_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.depo_tv_text_edit.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhExclusiveInputMask|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoEditMenu|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhNoTextHandles|QtCore.Qt.ImhPreferLatin|QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhSensitiveData|QtCore.Qt.ImhTime|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.depo_tv_text_edit.setObjectName("depo_tv_text_edit")
        self.depo_kulaklik_text_edit = QtWidgets.QTextEdit(self.Depo_urunler_Tab)
        self.depo_kulaklik_text_edit.setGeometry(QtCore.QRect(400, 110, 104, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.depo_kulaklik_text_edit.setFont(font)
        self.depo_kulaklik_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.depo_kulaklik_text_edit.setObjectName("depo_kulaklik_text_edit")
        self.depo_drone_text_edit = QtWidgets.QTextEdit(self.Depo_urunler_Tab)
        self.depo_drone_text_edit.setGeometry(QtCore.QRect(400, 140, 104, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.depo_drone_text_edit.setFont(font)
        self.depo_drone_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.depo_drone_text_edit.setObjectName("depo_drone_text_edit")
        self.depo_telefon_text_edit = QtWidgets.QTextEdit(self.Depo_urunler_Tab)
        self.depo_telefon_text_edit.setGeometry(QtCore.QRect(400, 170, 104, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.depo_telefon_text_edit.setFont(font)
        self.depo_telefon_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.depo_telefon_text_edit.setObjectName("depo_telefon_text_edit")
        self.muhasebe.addTab(self.Depo_urunler_Tab, "")
        self.urun_fiyatlar_Tab = QtWidgets.QWidget()
        self.urun_fiyatlar_Tab.setObjectName("urun_fiyatlar_Tab")
        self.urun_fiyatlar_baslik = QtWidgets.QLabel(self.urun_fiyatlar_Tab)
        self.urun_fiyatlar_baslik.setGeometry(QtCore.QRect(220, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.urun_fiyatlar_baslik.setFont(font)
        self.urun_fiyatlar_baslik.setObjectName("urun_fiyatlar_baslik")
        self.dizustu_fiyat_label = QtWidgets.QLabel(self.urun_fiyatlar_Tab)
        self.dizustu_fiyat_label.setGeometry(QtCore.QRect(50, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dizustu_fiyat_label.setFont(font)
        self.dizustu_fiyat_label.setObjectName("dizustu_fiyat_label")
        self.masaustu_fiyatlar_label = QtWidgets.QLabel(self.urun_fiyatlar_Tab)
        self.masaustu_fiyatlar_label.setGeometry(QtCore.QRect(50, 130, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.masaustu_fiyatlar_label.setFont(font)
        self.masaustu_fiyatlar_label.setObjectName("masaustu_fiyatlar_label")
        self.tv_label_fiyat = QtWidgets.QLabel(self.urun_fiyatlar_Tab)
        self.tv_label_fiyat.setGeometry(QtCore.QRect(50, 160, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tv_label_fiyat.setFont(font)
        self.tv_label_fiyat.setObjectName("tv_label_fiyat")
        self.kulaklik_label_fiyat = QtWidgets.QLabel(self.urun_fiyatlar_Tab)
        self.kulaklik_label_fiyat.setGeometry(QtCore.QRect(330, 90, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kulaklik_label_fiyat.setFont(font)
        self.kulaklik_label_fiyat.setObjectName("kulaklik_label_fiyat")
        self.drone_label_fiyat = QtWidgets.QLabel(self.urun_fiyatlar_Tab)
        self.drone_label_fiyat.setGeometry(QtCore.QRect(340, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.drone_label_fiyat.setFont(font)
        self.drone_label_fiyat.setObjectName("drone_label_fiyat")
        self.telefon_label_fiyat = QtWidgets.QLabel(self.urun_fiyatlar_Tab)
        self.telefon_label_fiyat.setGeometry(QtCore.QRect(330, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.telefon_label_fiyat.setFont(font)
        self.telefon_label_fiyat.setObjectName("telefon_label_fiyat")
        self.Urun_fiyatlari_buton_goster = QtWidgets.QPushButton(self.urun_fiyatlar_Tab)
        self.Urun_fiyatlari_buton_goster.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.Urun_fiyatlari_buton_goster.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";")
        self.Urun_fiyatlari_buton_goster.setObjectName("Urun_fiyatlari_buton_goster")
        self.fiyat_dizustu_text_edit = QtWidgets.QTextEdit(self.urun_fiyatlar_Tab)
        self.fiyat_dizustu_text_edit.setGeometry(QtCore.QRect(130, 90, 104, 21))
        self.fiyat_dizustu_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.fiyat_dizustu_text_edit.setObjectName("fiyat_dizustu_text_edit")
        self.fiyat_masaustu_text_edit = QtWidgets.QTextEdit(self.urun_fiyatlar_Tab)
        self.fiyat_masaustu_text_edit.setGeometry(QtCore.QRect(130, 120, 104, 21))
        self.fiyat_masaustu_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.fiyat_masaustu_text_edit.setObjectName("fiyat_masaustu_text_edit")
        self.fiyat_tv_text_edit = QtWidgets.QTextEdit(self.urun_fiyatlar_Tab)
        self.fiyat_tv_text_edit.setGeometry(QtCore.QRect(130, 150, 104, 21))
        self.fiyat_tv_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.fiyat_tv_text_edit.setObjectName("fiyat_tv_text_edit")
        self.fiyat_kulaklik_text_edit = QtWidgets.QTextEdit(self.urun_fiyatlar_Tab)
        self.fiyat_kulaklik_text_edit.setGeometry(QtCore.QRect(410, 90, 104, 21))
        self.fiyat_kulaklik_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.fiyat_kulaklik_text_edit.setObjectName("fiyat_kulaklik_text_edit")
        self.fiyat_drone_text_edit = QtWidgets.QTextEdit(self.urun_fiyatlar_Tab)
        self.fiyat_drone_text_edit.setGeometry(QtCore.QRect(410, 120, 104, 21))
        self.fiyat_drone_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.fiyat_drone_text_edit.setObjectName("fiyat_drone_text_edit")
        self.fiyat_telefon_text_edit = QtWidgets.QTextEdit(self.urun_fiyatlar_Tab)
        self.fiyat_telefon_text_edit.setGeometry(QtCore.QRect(410, 150, 104, 21))
        self.fiyat_telefon_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.fiyat_telefon_text_edit.setObjectName("fiyat_telefon_text_edit")
        self.muhasebe.addTab(self.urun_fiyatlar_Tab, "")
        self.Musteriler_tab = QtWidgets.QWidget()
        self.Musteriler_tab.setObjectName("Musteriler_tab")
        self.musteriler_baslik = QtWidgets.QLabel(self.Musteriler_tab)
        self.musteriler_baslik.setGeometry(QtCore.QRect(210, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.musteriler_baslik.setFont(font)
        self.musteriler_baslik.setObjectName("musteriler_baslik")
        self.isim_label_musteri = QtWidgets.QLabel(self.Musteriler_tab)
        self.isim_label_musteri.setGeometry(QtCore.QRect(70, 90, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.isim_label_musteri.setFont(font)
        self.isim_label_musteri.setObjectName("isim_label_musteri")
        self.soyisim_label_musteri = QtWidgets.QLabel(self.Musteriler_tab)
        self.soyisim_label_musteri.setGeometry(QtCore.QRect(310, 90, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.soyisim_label_musteri.setFont(font)
        self.soyisim_label_musteri.setObjectName("soyisim_label_musteri")
        self.musteriler_buton_goster = QtWidgets.QPushButton(self.Musteriler_tab)
        self.musteriler_buton_goster.setGeometry(QtCore.QRect(130, 210, 351, 23))
        self.musteriler_buton_goster.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.musteriler_buton_goster.setObjectName("musteriler_buton_goster")
        self.musteriler_soyad_text_edit = QtWidgets.QTextEdit(self.Musteriler_tab)
        self.musteriler_soyad_text_edit.setGeometry(QtCore.QRect(400, 70, 104, 121))
        self.musteriler_soyad_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.musteriler_soyad_text_edit.setObjectName("musteriler_soyad_text_edit")
        self.musteriler_isim_text_edit = QtWidgets.QTextEdit(self.Musteriler_tab)
        self.musteriler_isim_text_edit.setGeometry(QtCore.QRect(150, 70, 104, 121))
        self.musteriler_isim_text_edit.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.musteriler_isim_text_edit.setObjectName("musteriler_isim_text_edit")
        self.muhasebe.addTab(self.Musteriler_tab, "")
        self.musteri_kayit_tab = QtWidgets.QWidget()
        self.musteri_kayit_tab.setObjectName("musteri_kayit_tab")
        self.label = QtWidgets.QLabel(self.musteri_kayit_tab)
        self.label.setGeometry(QtCore.QRect(220, 20, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.isim_kayit_label = QtWidgets.QLabel(self.musteri_kayit_tab)
        self.isim_kayit_label.setGeometry(QtCore.QRect(180, 90, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.isim_kayit_label.setFont(font)
        self.isim_kayit_label.setObjectName("isim_kayit_label")
        self.isim_kayit_line = QtWidgets.QLineEdit(self.musteri_kayit_tab)
        self.isim_kayit_line.setGeometry(QtCore.QRect(260, 90, 113, 20))
        self.isim_kayit_line.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.isim_kayit_line.setObjectName("isim_kayit_line")
        self.soyisim_kayit_label = QtWidgets.QLabel(self.musteri_kayit_tab)
        self.soyisim_kayit_label.setGeometry(QtCore.QRect(180, 130, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.soyisim_kayit_label.setFont(font)
        self.soyisim_kayit_label.setObjectName("soyisim_kayit_label")
        self.soyisim_kayit_line = QtWidgets.QLineEdit(self.musteri_kayit_tab)
        self.soyisim_kayit_line.setGeometry(QtCore.QRect(260, 130, 113, 20))
        self.soyisim_kayit_line.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.soyisim_kayit_line.setObjectName("soyisim_kayit_line")
        self.musteri_kayit_buton = QtWidgets.QPushButton(self.musteri_kayit_tab)
        self.musteri_kayit_buton.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.musteri_kayit_buton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";")
        self.musteri_kayit_buton.setObjectName("musteri_kayit_buton")
        self.kayt_durum_label = QtWidgets.QLabel(self.musteri_kayit_tab)
        self.kayt_durum_label.setGeometry(QtCore.QRect(250, 160, 241, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.kayt_durum_label.setFont(font)
        self.kayt_durum_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.kayt_durum_label.setText("")
        self.kayt_durum_label.setObjectName("kayt_durum_label")
        self.muhasebe.addTab(self.musteri_kayit_tab, "")
        self.siparis_verme_tab = QtWidgets.QWidget()
        self.siparis_verme_tab.setObjectName("siparis_verme_tab")
        self.label_2 = QtWidgets.QLabel(self.siparis_verme_tab)
        self.label_2.setGeometry(QtCore.QRect(230, -10, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.urun_ismi_siparis_label = QtWidgets.QLabel(self.siparis_verme_tab)
        self.urun_ismi_siparis_label.setGeometry(QtCore.QRect(200, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.urun_ismi_siparis_label.setFont(font)
        self.urun_ismi_siparis_label.setObjectName("urun_ismi_siparis_label")
        self.urun_isim_siparis_line = QtWidgets.QLineEdit(self.siparis_verme_tab)
        self.urun_isim_siparis_line.setGeometry(QtCore.QRect(280, 70, 113, 20))
        self.urun_isim_siparis_line.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.urun_isim_siparis_line.setObjectName("urun_isim_siparis_line")
        self.urun_miktari_siparis_label = QtWidgets.QLabel(self.siparis_verme_tab)
        self.urun_miktari_siparis_label.setGeometry(QtCore.QRect(180, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.urun_miktari_siparis_label.setFont(font)
        self.urun_miktari_siparis_label.setObjectName("urun_miktari_siparis_label")
        self.urun_miktar_siparis_line = QtWidgets.QLineEdit(self.siparis_verme_tab)
        self.urun_miktar_siparis_line.setGeometry(QtCore.QRect(280, 120, 113, 20))
        self.urun_miktar_siparis_line.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.urun_miktar_siparis_line.setObjectName("urun_miktar_siparis_line")
        self.siparis_verme_durum = QtWidgets.QLabel(self.siparis_verme_tab)
        self.siparis_verme_durum.setGeometry(QtCore.QRect(200, 210, 191, 20))
        self.siparis_verme_durum.setText("")
        self.siparis_verme_durum.setObjectName("siparis_verme_durum")
        self.siparis_ver_buton = QtWidgets.QPushButton(self.siparis_verme_tab)
        self.siparis_ver_buton.setGeometry(QtCore.QRect(220, 150, 151, 23))
        self.siparis_ver_buton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";")
        self.siparis_ver_buton.setObjectName("siparis_ver_buton")
        self.siparis_durum = QtWidgets.QLabel(self.siparis_verme_tab)
        self.siparis_durum.setGeometry(QtCore.QRect(210, 180, 491, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.siparis_durum.setFont(font)
        self.siparis_durum.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.siparis_durum.setText("")
        self.siparis_durum.setObjectName("siparis_durum")
        self.muhasebe.addTab(self.siparis_verme_tab, "")

        self.retranslateUi(Muhasebe)
        self.muhasebe.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Muhasebe)

    def retranslateUi(self, Muhasebe):
        _translate = QtCore.QCoreApplication.translate
        Muhasebe.setWindowTitle(_translate("Muhasebe", "Muhasebe Programı"))
        self.Depoda_ki_urunler_baslik.setText(_translate("Muhasebe", "DEPODA Kİ ÜRÜNLER"))
        self.dizustu_label.setText(_translate("Muhasebe", "Dizüstü :"))
        self.masaustu_label.setText(_translate("Muhasebe", "Masaüstü : "))
        self.TV_label.setText(_translate("Muhasebe", "TV : "))
        self.kulaklik_label.setText(_translate("Muhasebe", "Kulaklık : "))
        self.drone_label.setText(_translate("Muhasebe", "Drone : "))
        self.telefon_label.setText(_translate("Muhasebe", "Telefon : "))
        self.depodaki_urunler_goster_buton.setText(_translate("Muhasebe", "Göster"))
        self.depo_dizustu_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:600;\"><br /></p></body></html>"))
        self.depo_masaustu_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:600;\"><br /></p></body></html>"))
        self.depo_tv_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:600;\"><br /></p></body></html>"))
        self.depo_kulaklik_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:600;\"><br /></p></body></html>"))
        self.depo_drone_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:600;\"><br /></p></body></html>"))
        self.depo_telefon_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:600;\"><br /></p></body></html>"))
        self.muhasebe.setTabText(self.muhasebe.indexOf(self.Depo_urunler_Tab), _translate("Muhasebe", "Depo Ürünler"))
        self.urun_fiyatlar_baslik.setText(_translate("Muhasebe", "ÜRÜN FİYATLARI"))
        self.dizustu_fiyat_label.setText(_translate("Muhasebe", "Dizüstü :"))
        self.masaustu_fiyatlar_label.setText(_translate("Muhasebe", "Masaüstü : "))
        self.tv_label_fiyat.setText(_translate("Muhasebe", "TV : "))
        self.kulaklik_label_fiyat.setText(_translate("Muhasebe", "Kulaklık : "))
        self.drone_label_fiyat.setText(_translate("Muhasebe", "Drone :"))
        self.telefon_label_fiyat.setText(_translate("Muhasebe", "Telefon : "))
        self.Urun_fiyatlari_buton_goster.setText(_translate("Muhasebe", "Göster"))
        self.fiyat_dizustu_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.fiyat_masaustu_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.fiyat_tv_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.fiyat_kulaklik_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.fiyat_drone_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.fiyat_telefon_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.muhasebe.setTabText(self.muhasebe.indexOf(self.urun_fiyatlar_Tab), _translate("Muhasebe", "Ürün Fiyatları"))
        self.musteriler_baslik.setText(_translate("Muhasebe", "MÜŞTERİLER"))
        self.isim_label_musteri.setText(_translate("Muhasebe", "İsim :"))
        self.soyisim_label_musteri.setText(_translate("Muhasebe", "Soyad : "))
        self.musteriler_buton_goster.setText(_translate("Muhasebe", "Göster"))
        self.musteriler_soyad_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.musteriler_isim_text_edit.setHtml(_translate("Muhasebe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.muhasebe.setTabText(self.muhasebe.indexOf(self.Musteriler_tab), _translate("Muhasebe", "Müşteriler"))
        self.label.setText(_translate("Muhasebe", "MÜŞTERİ KAYIT"))
        self.isim_kayit_label.setText(_translate("Muhasebe", "İsim : "))
        self.soyisim_kayit_label.setText(_translate("Muhasebe", "Soyisim : "))
        self.musteri_kayit_buton.setText(_translate("Muhasebe", "Kayıt Ol"))
        self.muhasebe.setTabText(self.muhasebe.indexOf(self.musteri_kayit_tab), _translate("Muhasebe", "Müşteri Kayıt"))
        self.label_2.setText(_translate("Muhasebe", "SİPARİŞ VERME"))
        self.urun_ismi_siparis_label.setText(_translate("Muhasebe", "Ürün İsmi : "))
        self.urun_miktari_siparis_label.setText(_translate("Muhasebe", "Ürün Miktarı :"))
        self.siparis_ver_buton.setText(_translate("Muhasebe", "Sipariş Ver"))
        self.muhasebe.setTabText(self.muhasebe.indexOf(self.siparis_verme_tab), _translate("Muhasebe", "Sipariş Verme"))
