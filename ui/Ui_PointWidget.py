# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PointWidget.ui'
#
# Created: Wed Dec 19 14:30:14 2012
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

class Ui_PointWidget(object):
    def setupUi(self, PointWidget):
        PointWidget.setObjectName(_fromUtf8("PointWidget"))
        PointWidget.resize(665, 558)
        self.verticalLayout = QtGui.QVBoxLayout(PointWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(PointWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(PointWidget)
        QtCore.QMetaObject.connectSlotsByName(PointWidget)

    def retranslateUi(self, PointWidget):
        PointWidget.setWindowTitle(_translate("PointWidget", "Punkteanzeige", None))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PointWidget", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PointWidget", "Punkte", None))

