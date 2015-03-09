# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow, QMessageBox, QLabel
from PyQt4.QtCore import pyqtSignature
import sys, cPickle, math
from ui.Ui_MainWindow import Ui_MainWindow
from src.DriverWidget import DriverWidget
from src.GroupWidget import GroupWidget
from src.PointWidget import PointWidget
from src.MatchWidget import MatchWidget


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.points = {0:3, 1:2, 2:1, 3:0}
        if len(sys.argv) > 1:
            self.data = sys.argv[2]
        else:
            self.data = "data.pkl"
        driver_list = []
        while len(driver_list) < 2:
            self.driver_widget = DriverWidget(driver_list)
            self.driver_widget.exec_()
            driver_list = self.driver_widget.drivers
        self.drivers = {}
        self.current = {}
        self.to_delete = {}
        for driver in driver_list:
            self.drivers[driver] = 0
        self.round = 0
        self.driven = set()
        self.left_gw = None
        self.right_gw = None
        self.add_group("left")
        if len(self.drivers) > 4:
            self.add_group("right")
        self.status_txt = None
        self.set_matches(math.ceil(len(self.drivers) / 4.))

    def set_matches(self, num):
        if self.status_txt:
            self.statusBar().removeWidget(self.status_txt)
        self.num_matches = num
        self.status_txt = QLabel("Anzahl verbleibender Spiele in dieser Runde: %.0f" % self.num_matches)
        self.statusBar().addWidget(self.status_txt)

    def add_group(self, place):
        """
        Add a single group.
        """
        diff = set(self.drivers) - self.driven
        rest = len(self.drivers) % 4
        if len(self.driven) < 9 and rest:
            if rest == 3:
                if len(self.driven) < 3:
                    num = 3
                else:
                    num = 4

            elif rest == 2:
                if len(self.driven) < 4:
                    num = 3
                else:
                    num = 4

            elif rest == 1:
                num = 3
        else:
            num = 4

        srtd = sorted(diff, key=self.drivers.get)
        sub = srtd[:num]
        for dr in sub:
            self.current[dr] = place
        self.driven = self.driven.union(sub)
        if place == "left":
            self.left_gw = GroupWidget(sub, place)
            self.left_gw.pushButton.released.connect(self.left_decided)
            self.horizontalLayout.insertWidget(0, self.left_gw)
        else:
            self.right_gw = GroupWidget(sub, place)
            self.right_gw.pushButton.released.connect(self.right_decided)
            self.horizontalLayout.insertWidget(1, self.right_gw)

    def left_decided(self):
        """
        Wrapper for left.
        """
        self.decided(self.sender().parent().parent(), "left")

    def right_decided(self):
        """
        Wrapper for right.
        """
        self.decided(self.sender().parent().parent(), "right")

    def decided(self, source, place):
        """
        Handle result.
        """
        if source.radio:
            self.drivers[str(source.name1.text())] += self.points[source.place1 - 1]
            try:
                self.drivers[str(source.name2.text())] += self.points[source.place2 - 1]
                self.drivers[str(source.name3.text())] += self.points[source.place3 - 1]
                self.drivers[str(source.name4.text())] += self.points[source.place4 - 1]
            except KeyError: # It is not always certain that more than one player is scheduled to play
                pass
        else:
            self.drivers[str(source.name1.text())] += self.points[source.rank_combo1.currentIndex()]
            try:
                self.drivers[str(source.name2.text())] += self.points[source.rank_combo2.currentIndex()]
                self.drivers[str(source.name3.text())] += self.points[source.rank_combo3.currentIndex()]
                self.drivers[str(source.name4.text())] += self.points[source.rank_combo4.currentIndex()]
            except KeyError: # It is not always certain that more than one player is scheduled to play
                pass
        f = open(self.data, "w")
        cPickle.dump(self.drivers, f, protocol=cPickle.HIGHEST_PROTOCOL)
        f.close()
        source.close()
        for delete in self.to_delete.keys():
            if self.to_delete[delete] == place:
                del(self.drivers[delete])
                del(self.to_delete[delete])
        self.set_matches(math.ceil((len(self.drivers) - len(self.driven)) / 4.) + 1)
        if place == "left":
            self.left_gw = None
        else:
            self.right_gw = None
        if len(set(self.drivers) - self.driven) > 0:
            self.add_group(place)
        else:
            if not (self.left_gw or self.right_gw):
                msg_box = QMessageBox(4, "Noch eine Runde?", "Wollt ihr noch eine Runde spielen (sonst seht ihr das Ergebnis)?")
                msg_box.addButton("Ja!", QMessageBox.YesRole)
                msg_box.addButton("Nein :(", QMessageBox.NoRole)
                res = msg_box.exec_()
                if res:
                    self.show_result()
                else:
                    self.round += 1
                    self.driven = set()
                    self.set_matches(math.ceil((len(self.drivers) - len(self.driven)) / 4.))
                    self.add_group("left")
                    if len(self.drivers) > 4:
                        self.add_group("right")

    def show_result(self):
        """
        Show names and points.
        """
        self.point_widget = PointWidget(self.drivers)
        self.point_widget.show()

    @pyqtSignature("")
    def on_actionPunkteanzeige_triggered(self):
        """
        Calls the appropriate method if "Punkteanzeige" in the menu is clicked.
        """
        self.show_result()

    @pyqtSignature("")
    def on_actionNaechste_Matches_triggered(self):
        """
        Calls the appropriate method if "Nächste Matches" in the menu is clicked.
        """
        self.match_widget = MatchWidget(self.drivers, self.driven)
        self.match_widget.show()

    @pyqtSignature("")
    def on_actionBeenden_triggered(self):
        """
        Calls the appropriate method if "Beenden" in the menu is clicked.
        """
        self.close()

    @pyqtSignature("")
    def on_actionSpieler_hinzufuegen_triggered(self):
        """
        Calls the appropriate method if "Spieler löschen" in the menu is clicked.
        """
        self.driver_widget = DriverWidget([])
        self.driver_widget.exec_()
        driver_list = self.driver_widget.drivers
        for driver in driver_list:
            self.drivers[driver] = 0

    @pyqtSignature("")
    def on_actionSpieler_loeschen_triggered(self):
        """
        Calls the appropriate method if "Spieler hinzufügen" in the menu is clicked.
        """
        self.driver_widget = DriverWidget(self.drivers, delete=True)
        self.driver_widget.exec_()
        driver_list = self.driver_widget.drivers
        tmp = {}
        for driver in driver_list:
            tmp[driver] = self.drivers[driver]
        for driver in self.current:
            if not driver in tmp:
                self.to_delete[driver] = self.current[driver]
                tmp[driver] = self.drivers[driver]
        self.drivers = tmp
