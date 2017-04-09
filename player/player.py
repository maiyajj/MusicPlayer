# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created: Sun Apr 09 16:06:15 2017
#      by: PyQt4 UI code generator 4.11.3
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


class Ui_TrayIcon(object):
    def setupUi(self, TrayIcon):
        TrayIcon.setObjectName(_fromUtf8("TrayIcon"))
        TrayIcon.resize(618, 75)
        self.verticalLayout = QtGui.QVBoxLayout(TrayIcon)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBoxMessages = QtGui.QGroupBox(TrayIcon)
        self.groupBoxMessages.setEnabled(True)
        self.groupBoxMessages.setObjectName(_fromUtf8("groupBoxMessages"))
        self.gridLayout = QtGui.QGridLayout(self.groupBoxMessages)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.groupBoxMessages)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEditTitle = QtGui.QLineEdit(self.groupBoxMessages)
        self.lineEditTitle.setObjectName(_fromUtf8("lineEditTitle"))
        self.horizontalLayout.addWidget(self.lineEditTitle)
        self.open_file = QtGui.QPushButton(self.groupBoxMessages)
        self.open_file.setMaximumSize(QtCore.QSize(75, 16777215))
        self.open_file.setObjectName(_fromUtf8("open_file"))
        self.horizontalLayout.addWidget(self.open_file)
        self.startmp3 = QtGui.QPushButton(self.groupBoxMessages)
        self.startmp3.setMaximumSize(QtCore.QSize(75, 16777215))
        self.startmp3.setObjectName(_fromUtf8("startmp3"))
        self.horizontalLayout.addWidget(self.startmp3)
        self.kaijiqidong = QtGui.QRadioButton(self.groupBoxMessages)
        self.kaijiqidong.setObjectName(_fromUtf8("kaijiqidong"))
        self.horizontalLayout.addWidget(self.kaijiqidong)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxMessages)

        self.retranslateUi(TrayIcon)
        QtCore.QObject.connect(self.open_file, QtCore.SIGNAL(_fromUtf8("clicked()")), TrayIcon.open_path)
        QtCore.QObject.connect(self.startmp3, QtCore.SIGNAL(_fromUtf8("clicked()")), TrayIcon.start)
        QtCore.QObject.connect(self.kaijiqidong, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), TrayIcon.kaiji)
        QtCore.QMetaObject.connectSlotsByName(TrayIcon)

    def retranslateUi(self, TrayIcon):
        TrayIcon.setWindowTitle(_translate("TrayIcon", "播放音频", None))
        self.groupBoxMessages.setTitle(_translate("TrayIcon", "音频播放", None))
        self.label_5.setText(_translate("TrayIcon", "播放音频：", None))
        self.open_file.setText(_translate("TrayIcon", "选择文件", None))
        self.startmp3.setText(_translate("TrayIcon", "开始", None))
        self.kaijiqidong.setText(_translate("TrayIcon", "开机启动", None))
