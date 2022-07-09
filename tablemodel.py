from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt


class FixedColumnDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, defaultWidth=None, parent=None):
        QtWidgets.QStyledItemDelegate.__init__(self, parent)
        self.defaultWidth = defaultWidth

    def sizeHint(self, option, index):
        hint = self.sizeHint(self, option, index)
        if self.defaultWidth is not None:
            hint.setWidth(self.defaultWidth)
        return hint


class TableModel(QtCore.QAbstractTableModel):
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            # return f"Column {section + 1}"
            return self.columns[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return f"{section + 1}"

    def __init__(self, data, columns):
        self.columns = columns
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        if role == Qt.TextAlignmentRole:
            return Qt.AlignHCenter + Qt.AlignVCenter


    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
