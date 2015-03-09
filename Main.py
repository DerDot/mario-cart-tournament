#!/usr/bin/python

from PyQt4.QtGui import QApplication
from src.MainWindow import MainWindow
import locale

def main():
    """
    A script to call the VKPMainWindow and execute it as a QApplication.
    """
    import sys
    QApplication.setGraphicsSystem("raster")
    app = QApplication(sys.argv)
    app.setApplicationName('MKT')
    app.setOrganizationName("AStA-Film");
    locale.setlocale(locale.LC_NUMERIC, 'C')
    wnd = MainWindow()
    wnd.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
