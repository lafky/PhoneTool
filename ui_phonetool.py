# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phonetool.ui'
#
# Created: Tue Sep 30 19:19:40 2014
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_PhoneTool(object):
    def setupUi(self, PhoneTool):
        PhoneTool.setObjectName(_fromUtf8("PhoneTool"))
        PhoneTool.resize(957, 338)
        PhoneTool.setMouseTracking(True)
        self.centralwidget = QtGui.QWidget(PhoneTool)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(20, 130, 921, 171))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.addButton = QtGui.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(650, 50, 191, 31))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.searchField = QtGui.QLineEdit(self.centralwidget)
        self.searchField.setGeometry(QtCore.QRect(20, 50, 261, 31))
        self.searchField.setObjectName(_fromUtf8("searchField"))
        self.searchField_2 = QtGui.QLineEdit(self.centralwidget)
        self.searchField_2.setGeometry(QtCore.QRect(330, 50, 261, 31))
        self.searchField_2.setObjectName(_fromUtf8("searchField_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 261, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 100, 211, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        PhoneTool.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(PhoneTool)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PhoneTool.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(PhoneTool)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 957, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.File = QtGui.QMenu(self.menuBar)
        self.File.setObjectName(_fromUtf8("File"))
        PhoneTool.setMenuBar(self.menuBar)
        self.actionExit = QtGui.QAction(PhoneTool)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.File.addAction(self.actionExit)
        self.menuBar.addAction(self.File.menuAction())

        self.retranslateUi(PhoneTool)
        QtCore.QMetaObject.connectSlotsByName(PhoneTool)

    def retranslateUi(self, PhoneTool):
        PhoneTool.setWindowTitle(_translate("PhoneTool", "Phone Tool", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PhoneTool", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PhoneTool", "Office", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PhoneTool", "Cell", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("PhoneTool", "Home", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("PhoneTool", "Pager", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("PhoneTool", "Preference", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("PhoneTool", "Notes", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("PhoneTool", "Group", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("PhoneTool", "Supervisor", None))
        self.addButton.setToolTip(_translate("PhoneTool", "Add or edit an entry to the Phone Tool (tm) database", None))
        self.addButton.setText(_translate("PhoneTool", "Add/Update/Delete Contact", None))
        self.label.setText(_translate("PhoneTool", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Search By Name:</span></p></body></html>", None))
        self.label_2.setText(_translate("PhoneTool", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Search By Group:</span></p></body></html>", None))
        self.checkBox.setText(_translate("PhoneTool", "Select to make table editable", None))
        self.File.setTitle(_translate("PhoneTool", "File", None))
        self.actionExit.setText(_translate("PhoneTool", "Exit", None))
        self.actionExit.setShortcut(_translate("PhoneTool", "Esc", None))

