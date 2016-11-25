# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_items.ui'
#
# Created: Fri Nov 25 13:05:59 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from view_details import dbase_results_gui_args


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_ViewItems(object):

    def dbase_results(self):
        customer_name = self.lineEdit.text()
        allSQLRows = dbase_results_gui_args(customer_name)
        self.tableWidget.setRowCount(len(allSQLRows))  ##set number of rows
        self.tableWidget.setColumnCount(3)  ## set number of columns

        for x in range(0, len(allSQLRows)):
            r = allSQLRows[x]
            for col in range(0, 3):
                self.tableWidget.setItem(x, col, QtGui.QTableWidgetItem(str(r[col])))

    def clear_text(self):
        self.lineEdit.setText("ALL")
        self.dbase_results()
        self.lineEdit.clear()

    def setupUi(self, Dialog3):
        Dialog3.setObjectName(_fromUtf8("Dialog3"))
        Dialog3.resize(380, 526)
        self.tableWidget = QtGui.QTableWidget(Dialog3)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 340, 401))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_1 = QtGui.QPushButton(Dialog3)
        self.pushButton_1.setGeometry(QtCore.QRect(140, 20, 41, 25))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.lineEdit = QtGui.QLineEdit(Dialog3)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(Dialog3)
        self.pushButton_2.setGeometry(QtCore.QRect(187, 20, 51, 26))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog3)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 490, 91, 26))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi3(Dialog3)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), Dialog3.accept)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.clear_text)
        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL("clicked()"), self.dbase_results)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi3(self, Dialog3):
        Dialog3.setWindowTitle(_translate("Dialog3", "Dialog3", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog3", "ItemID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog3", "Item Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog3", "Price", None))
        self.pushButton_1.setText(_translate("Dialog3", "Find", None))
        self.pushButton_2.setText(_translate("Dialog3", "Clear", None))
        self.pushButton_3.setText(_translate("Dialog3", "OK", None))
        self.lineEdit.setText("ALL")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog3 = QtGui.QDialog()
    ui = Ui_ViewItems()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())

