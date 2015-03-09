# -*- coding: utf-8 -*-

"""
Module implementing DriverWidget.
"""

from PyQt4.QtGui import QDialog, QPushButton, QLineEdit, QHBoxLayout
from PyQt4.QtCore import pyqtSignature, Qt
from ui.Ui_DriverWidget import Ui_DriverWidget
import sys

class DriverWidget(QDialog, Ui_DriverWidget):

    def __init__(self, existing=None, delete=False, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        if not existing:
            existing = {}
        try:
            self.drivers = existing.keys()
        except AttributeError: # This is probably a list not a dict
            self.drivers = existing
        for name in existing:
            self.add_neg_line(name)
        if not delete:
            self.add_line()
        if sys.platform.startswith("linux"):
            self.encoding = "utf8"
        else:
            self.encoding = "iso8859"

    @pyqtSignature("")
    def line_triggered(self):
        """
        What to do if enter is pressed in the lineedit.
        """
        line_edit = self.sender()
        button = line_edit.button
        self.triggered(button, line_edit)

    @pyqtSignature("")
    def plus_triggered(self):
        """
        What to do if plus is triggered.
        """
        button = self.sender()
        line_edit = self.sender().line_edit
        self.triggered(button, line_edit)

    def triggered(self, button, line_edit):
        """
        Handle both button and lineedit.
        """
        if button.text() == "+":
            if line_edit.text():
                if not line_edit.text() in self.drivers:
                    button.setText("-")
                    self.drivers.append(unicode(line_edit.text(), encoding=self.encoding))
                    line_edit.setEnabled(False)
                    self.add_line()
        else:
            layout = button.layout()
            self.drivers.remove(str(line_edit.text()))
            button.setParent(None)
            line_edit.setParent(None)
            self.verticalLayout_2.removeItem(layout)


    def add_line(self):
        """
        Add a new line.
        """
        layout = QHBoxLayout()
        le = LineEdit()
        le.returnPressed.connect(self.line_triggered)
        pbutton = PlusButton(le)
        pbutton.released.connect(self.plus_triggered)
        le.button = pbutton
        layout.addWidget(le)
        layout.addWidget(pbutton)
        self.verticalLayout_2.insertLayout(0, layout)
        le.setFocus()

    def add_neg_line(self, name):
        """
        Add a new negative line.
        """
        layout = QHBoxLayout()
        le = LineEdit()
        le.setText(name)
        le.setEnabled(False)
        le.returnPressed.connect(self.line_triggered)
        pbutton = PlusButton(le)
        pbutton.setText("-")
        pbutton.released.connect(self.plus_triggered)
        le.button = pbutton
        layout.addWidget(le)
        layout.addWidget(pbutton)
        self.verticalLayout_2.insertLayout(0, layout)
        le.setFocus()

    def keyPressEvent(self, event):
        if event.key() != 16777220:
            QDialog.keyPressEvent(self, event)

    @pyqtSignature("")
    def on_okButton_released(self):
        """
        """
        self.close()

class PlusButton(QPushButton):
    """
    Special button.
    """
    def __init__(self, line_edit, parent=None):
        QPushButton.__init__(self, parent)
        self.line_edit = line_edit
        self.setText("+")

class LineEdit(QLineEdit):
    """
    Special lineedit.
    """
    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent)
        self.button = None

