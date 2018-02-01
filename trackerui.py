#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

This example shows a tooltip on
a window and a button

author: Jan Bodnar
website: http://zetcode.com/gui/pysidetutorial/
last edited: August 2011
"""

import sys
from PySide import QtGui, QtCore


class TimeTrackerUi(QtGui.QWidget):

    def __init__(self):
        super(TimeTrackerUi, self).__init__()

        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>Time Tracker UI</b> widget')

        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 100)

        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Time Tracker UI')
        self.setWindowIcon(QtGui.QIcon('trackerui.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = TimeTrackerUi()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()