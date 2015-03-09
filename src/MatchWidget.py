# -*- coding: utf-8 -*-

"""
Module implementing DriverWidget.
"""

from PyQt4.QtGui import QDialog, QListWidgetItem
from ui.Ui_MatchWidget import Ui_MatchWidget
import copy


class MatchWidget(QDialog, Ui_MatchWidget):

    def __init__(self, drivers, driven, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.drivers = copy.deepcopy(drivers)
        self.driven = copy.deepcopy(driven)

        diff = set(self.drivers) - self.driven
        while diff:
            diff = set(self.drivers) - self.driven
            if len(diff) < 8:
                if len(diff) <= 4:
                    num = len(diff)
                else:
                    num = len(diff) - len(diff) / 2
            else:
                num = 4
            srtd = sorted(diff, key=self.drivers.get)
            sub = srtd[:num]
            self.driven = self.driven.union(sub)
            self.add_group(sub)

    def add_group(self, sub):
        item = QListWidgetItem(", ".join(sub))
        self.listWidget.addItem(item)

    def on_ok_button_released(self):
        self.close()
