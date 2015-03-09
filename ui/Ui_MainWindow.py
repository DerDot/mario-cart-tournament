# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Wed Dec 19 10:52:19 2012
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 524, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDatei = QtGui.QMenu(self.menubar)
        self.menuDatei.setObjectName(_fromUtf8("menuDatei"))
        self.menuBearbeiten = QtGui.QMenu(self.menubar)
        self.menuBearbeiten.setObjectName(_fromUtf8("menuBearbeiten"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionBeenden = QtGui.QAction(MainWindow)
        self.actionBeenden.setObjectName(_fromUtf8("actionBeenden"))
        self.actionSpieler_hinzufuegen = QtGui.QAction(MainWindow)
        self.actionSpieler_hinzufuegen.setObjectName(_fromUtf8("actionSpieler_hinzufuegen"))
        self.actionSpieler_loeschen = QtGui.QAction(MainWindow)
        self.actionSpieler_loeschen.setObjectName(_fromUtf8("actionSpieler_loeschen"))
        self.actionPunkteanzeige = QtGui.QAction(MainWindow)
        self.actionPunkteanzeige.setObjectName(_fromUtf8("actionPunkteanzeige"))
        self.actionNaechste_Matches = QtGui.QAction(MainWindow)
        self.actionNaechste_Matches.setObjectName(_fromUtf8("actionNaechste_Matches"))
        self.menuDatei.addAction(self.actionBeenden)
        self.menuBearbeiten.addAction(self.actionSpieler_hinzufuegen)
        self.menuBearbeiten.addAction(self.actionSpieler_loeschen)
        self.menuBearbeiten.addSeparator()
        self.menuBearbeiten.addAction(self.actionPunkteanzeige)
        self.menuBearbeiten.addAction(self.actionNaechste_Matches)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuBearbeiten.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mario Kart Turnier", None))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei", None))
        self.menuBearbeiten.setTitle(_translate("MainWindow", "Bearbeiten", None))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden", None))
        self.actionSpieler_hinzufuegen.setText(_translate("MainWindow", "Spieler hinzufügen", None))
        self.actionSpieler_loeschen.setText(_translate("MainWindow", "Spieler löschen", None))
        self.actionPunkteanzeige.setText(_translate("MainWindow", "Punkteanzeige", None))
        self.actionNaechste_Matches.setText(_translate("MainWindow", "Nächste Matches", None))

