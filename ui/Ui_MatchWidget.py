# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MatchWidget.ui'
#
# Created: Wed Dec 19 13:08:56 2012
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

class Ui_MatchWidget(object):
    def setupUi(self, MatchWidget):
        MatchWidget.setObjectName(_fromUtf8("MatchWidget"))
        MatchWidget.resize(490, 387)
        self.verticalLayout = QtGui.QVBoxLayout(MatchWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(MatchWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtGui.QPushButton(MatchWidget)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MatchWidget)
        QtCore.QMetaObject.connectSlotsByName(MatchWidget)

    def retranslateUi(self, MatchWidget):
        MatchWidget.setWindowTitle(_translate("MatchWidget", "Nächste Matches", None))
        self.ok_button.setText(_translate("MatchWidget", "OK", None))

