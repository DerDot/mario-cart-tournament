# -*- coding: utf-8 -*-

"""
Module implementing DriverWidget.
"""

from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignature
from ui.Ui_GroupWidgetRadio import Ui_GroupWidget

class GroupWidget(QWidget, Ui_GroupWidget):

    def __init__(self, drivers, place, parent=None):
        """
        Constructor
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
        direction = {"left": "links", "right": "rechts"}
        self.group_label.setText("Gruppe %s:" % direction[place])
        self.name1.setText(drivers[0])
        try:
            self.name2.setText(drivers[1])
            self.name3.setText(drivers[2])
            self.name4.setText(drivers[3])
        except IndexError:
            pass
        self.place1 = 1
        self.place2 = 1
        self.place3 = 1
        self.place4 = 1
        global radio
        self.radio = radio

    @pyqtSignature("bool")
    def on_radio11_toggled(self, checked):
        if checked:
            self.place1 = 1

    @pyqtSignature("bool")
    def on_radio21_toggled(self, checked):
        if checked:
            self.place2 = 1

    @pyqtSignature("bool")
    def on_radio31_toggled(self, checked):
        if checked:
            self.place3 = 1

    @pyqtSignature("bool")
    def on_radio41_toggled(self, checked):
        if checked:
            self.place4 = 1

    @pyqtSignature("bool")
    def on_radio12_toggled(self, checked):
        if checked:
            self.place1 = 2

    @pyqtSignature("bool")
    def on_radio22_toggled(self, checked):
        if checked:
            self.place2 = 2

    @pyqtSignature("bool")
    def on_radio32_toggled(self, checked):
        if checked:
            self.place3 = 2

    @pyqtSignature("bool")
    def on_radio42_toggled(self, checked):
        if checked:
            self.place4 = 2

    @pyqtSignature("bool")
    def on_radio13_toggled(self, checked):
        if checked:
            self.place1 = 3

    @pyqtSignature("bool")
    def on_radio23_toggled(self, checked):
        if checked:
            self.place2 = 3

    @pyqtSignature("bool")
    def on_radio33_toggled(self, checked):
        if checked:
            self.place3 = 3

    @pyqtSignature("bool")
    def on_radio43_toggled(self, checked):
        if checked:
            self.place4 = 3

    @pyqtSignature("bool")
    def on_radio14_toggled(self, checked):
        if checked:
            self.place1 = 4

    @pyqtSignature("bool")
    def on_radio24_toggled(self, checked):
        if checked:
            self.place2 = 4

    @pyqtSignature("bool")
    def on_radio34_toggled(self, checked):
        if checked:
            self.place3 = 4

    @pyqtSignature("bool")
    def on_radio44_toggled(self, checked):
        if checked:
            self.place4 = 4

