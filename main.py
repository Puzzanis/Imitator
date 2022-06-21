import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidgetItem
from PyQt5 import uic, QtCore, QtWidgets, QtGui

import branch as brn
from dialog_window import ClssDialog


class App(QWidget):
    table_general = []  # list of all added objects

    def __init__(self):
        super().__init__()
        self.d = {'TestName': {'Ref': 'ABC/DEF', 'Property': [{'Number': '2', 'Zipcode': '0002234',
                                                               'KeyAvailable': 'Yes'}, {'Number': '3',
                                                                                        'Zipcode': '2342444'}]}}
        self.curElement = ''
        self.start()

    def start(self):
        self.ui = uic.loadUi("untitled.ui")
        self.tooltip()
        self.table = self.ui.tableView
        self.tree = self.ui.treeWidget
        self.tree.setStyleSheet(brn.STYLESHEET)
        self.tree.setCurrentItem(self.tree.topLevelItem(0))
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.on_context_menu)
        self.ui.pushButton_7.clicked.connect(self.add)
        self.tree.itemClicked.connect(self.click)
        self.start_table()
        self.ui.show()

    def tooltip(self):
        self.ui.pushButton.setToolTip('Создать новую модель')
        self.ui.pushButton_2.setToolTip('Открыть ранее сохраненную модель из файла')
        self.ui.pushButton_3.setToolTip('Сохранить модель в файл')
        self.ui.pushButton_4.setToolTip('Поверх всех окон')
        self.ui.pushButton_5.setToolTip('Отменить')
        self.ui.pushButton_6.setToolTip('Повторить')
        self.ui.pushButton_7.setToolTip('Добавить объект или строку в таблице')
        self.ui.pushButton_8.setToolTip('Удалить объект или строку в таблице')
        self.ui.pushButton_9.setToolTip('Вырезать')
        self.ui.pushButton_10.setToolTip('Копировать')
        self.ui.pushButton_11.setToolTip('Вставить')
        self.ui.pushButton_12.setToolTip('Запустить')
        self.ui.pushButton_13.setToolTip('Пауза')
        self.ui.pushButton_14.setToolTip('Остановить выполнение')

    def on_context_menu(self, point):
        self.popMenu = QtWidgets.QMenu()
        context = ['Отменить', 'Повторить', 'Добавить', 'Удалить', 'Вырезать', 'Копировать', 'Вставить', 'Изменить название',
             'Блокировка', 'Открыть в отдельном окне...']
        icon = ['icon/back.png', 'icon/back_forward.png', 'icon/insert_new_add_21481.png', 'icon/minus_21480.png',
                'icon/scissors_cut_19670.png', 'icon/1455554314_line-15_icon-icons.com_53330.png',
                'icon/folder-10_icon-icons.com_62068.png', '', '', '']
        def_list = [self.back, self.forward, self.add, self.delete, self.cut, self.copy, self.insert, self.rename,
                    self.block, self.open_new_window]
        for i, b, d in zip(context, icon, def_list):
            self.addDes = QtWidgets.QAction(QtGui.QIcon(b), i, self.popMenu)
            self.addDes.triggered.connect(d)
            self.addDes.setEnabled(False) if i == context[1] else self.addDes.setEnabled(True)  # for example
            self.popMenu.addAction(self.addDes)
        a = self.tree.itemAt(point)
        # print(self.tree.currentItem().text(0))
        if a is not None:
            self.popMenu.exec_(self.tree.viewport().mapToGlobal(point))

    def tree_from_dict(self, data=None, parent=None):
        for key, value in data.items():
            item = QTreeWidgetItem(parent)

            item.setText(0, key)

            if isinstance(value, dict):
                self.tree_from_dict(data=value, parent=item)
            elif isinstance(value, list):
                [self.tree_from_dict(i, parent=item) for idx, i in enumerate(value)]

            else:
                item.setText(1, value)

    def remove_child(self, parent=None):
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)

    def click(self):
        pass

    def start_table(self):
        self.model = QtGui.QStandardItemModel(1, 2)
        self.model.setHorizontalHeaderLabels(['№', 'Название'])
        self.model.setItem(0, 0, QtGui.QStandardItem('%d' % 1))
        self.model.verticalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignHCenter)
        self.table.setModel(self.model)

    def back(self):
        print('ok')

    def forward(self):
        print('ok1')

    def add(self):
        dialog = ClssDialog(self)
        dialog.ui.show()
        dialog.ui.exec_()
        self.table_general.append(self.curElement)

    def delete(self):
        self.remove_child(parent=self.tree.currentItem())
        print('ok3')

    def cut(self):
        print('ok4')

    def copy(self):
        print('ok5')

    def insert(self):
        print('ok6')

    def rename(self):
        print('ok7')

    def block(self):
        print('ok8')

    def open_new_window(self):
        print('ok9')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
