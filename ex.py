import sys
from PyQt5.QtWidgets import *

class Window(QTreeWidget):
    def __init__(self):
        super().__init__()
        style = QApplication.style()
        self.dir_open = style.standardIcon(QStyle.SP_DirOpenIcon)
        self.dir_closed = style.standardIcon(QStyle.SP_DirClosedIcon)
        self.file_all = style.standardIcon(QStyle.SP_FileIcon)
        for index in '1234':
            parent = QTreeWidgetItem(self, ['Dir' + index])
            parent.setIcon(0, self.dir_closed)
            for item in 'ABC':
                child = QTreeWidgetItem(parent, ['File' + index + item])
                child.setIcon(0, self.file_all)
        self.itemExpanded.connect(self.handleExpanded)
        self.itemCollapsed.connect(self.handleCollapsed)

    def handleExpanded(self, item):
        item.setIcon(0, self.dir_open)

    def handleCollapsed(self, item):
        item.setIcon(0, self.dir_closed)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 50, 400, 300)
    window.show()
    sys.exit(app.exec_())