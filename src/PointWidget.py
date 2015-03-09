# -*- coding: utf-8 -*-

"""
Module implementing DriverWidget.
"""

from PyQt4.QtGui import QDialog, QTableWidgetItem
from PyQt4.QtCore import Qt
from ui.Ui_PointWidget import Ui_PointWidget


class PointWidget(QDialog, Ui_PointWidget):

    def __init__(self, drivers, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.tableWidget.setRowCount(len(drivers))
        for idx, driver in enumerate(drivers):
            name = QTableWidgetItem(driver)
            points = QTableWidgetItem(str(drivers[driver]))
            self.tableWidget.setItem(idx, 0, name)
            self.tableWidget.setItem(idx, 1, points)
        self.tableWidget.sortByColumn(1)
