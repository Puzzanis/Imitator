from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication
import sys

import branch as brn


folders = ['Логические', 'Переключатели', 'ModBus', 'Преобразователи', 'Генераторы']


class ClssDialog(QtWidgets.QDialog):

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root
        self.start()

    def start(self):
        self.ui = uic.loadUi("dialogmenu.ui")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.tree = self.ui.treeWidget
        self.tree.setCurrentItem(self.tree.topLevelItem(0))
        self.tree.setStyleSheet(brn.STYLESHEET)
        self.okBtn = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        self.tree.itemClicked.connect(self.clickOff)
        self.ui.buttonBox.accepted.connect(self.prt)
        self.clickOff()

    def clickOff(self):
        if self.tree.currentItem().text(0) in folders:
            self.okBtn.setEnabled(False)
        else:
            self.tree.doubleClicked.connect(self.prt)
            self.okBtn.setEnabled(True)

    def prt(self):
        self.main.curElement = self.tree.currentItem().text(0)
        self.ui.close()

