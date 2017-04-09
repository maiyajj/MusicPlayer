# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ‘trayicon.ui‘
#
# Created: Tue Mar 03 17:34:43 2015
#      by: PyQt4 UI code generator 4.10.3
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
        TrayIcon.resize(418, 441)
        TrayIcon.setMaximumSize(QtCore.QSize(1024, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(TrayIcon)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBoxTrayIcon = QtGui.QGroupBox(TrayIcon)
        self.groupBoxTrayIcon.setMinimumSize(QtCore.QSize(400, 100))
        self.groupBoxTrayIcon.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBoxTrayIcon.setObjectName(_fromUtf8("groupBoxTrayIcon"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBoxTrayIcon)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayoutByrayicon = QtGui.QHBoxLayout()
        self.horizontalLayoutByrayicon.setObjectName(_fromUtf8("horizontalLayoutByrayicon"))
        self.label = QtGui.QLabel(self.groupBoxTrayIcon)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayoutByrayicon.addWidget(self.label)
        self.comboBoxIcon = QtGui.QComboBox(self.groupBoxTrayIcon)
        self.comboBoxIcon.setObjectName(_fromUtf8("comboBoxIcon"))
        self.horizontalLayoutByrayicon.addWidget(self.comboBoxIcon)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutByrayicon.addItem(spacerItem)
        self.checkBoxShowIcon = QtGui.QCheckBox(self.groupBoxTrayIcon)
        self.checkBoxShowIcon.setObjectName(_fromUtf8("checkBoxShowIcon"))
        self.horizontalLayoutByrayicon.addWidget(self.checkBoxShowIcon)
        self.verticalLayout_2.addLayout(self.horizontalLayoutByrayicon)
        self.checkBoxQQmsg = QtGui.QCheckBox(self.groupBoxTrayIcon)
        self.checkBoxQQmsg.setObjectName(_fromUtf8("checkBoxQQmsg"))
        self.verticalLayout_2.addWidget(self.checkBoxQQmsg)
        self.verticalLayout.addWidget(self.groupBoxTrayIcon)
        self.groupBoxMessages = QtGui.QGroupBox(TrayIcon)
        self.groupBoxMessages.setEnabled(True)
        self.groupBoxMessages.setObjectName(_fromUtf8("groupBoxMessages"))
        self.gridLayout = QtGui.QGridLayout(self.groupBoxMessages)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.groupBoxMessages)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBoxMessages)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.textEditContent = QtGui.QTextEdit(self.groupBoxMessages)
        self.textEditContent.setObjectName(_fromUtf8("textEditContent"))
        self.gridLayout.addWidget(self.textEditContent, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBoxMessages)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.comboBox_MsgInfo = QtGui.QComboBox(self.groupBoxMessages)
        self.comboBox_MsgInfo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_MsgInfo.setObjectName(_fromUtf8("comboBox_MsgInfo"))
        self.gridLayout.addWidget(self.comboBox_MsgInfo, 0, 2, 1, 1)
        self.spinBoxTime = QtGui.QSpinBox(self.groupBoxMessages)
        self.spinBoxTime.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxTime.sizePolicy().hasHeightForWidth())
        self.spinBoxTime.setSizePolicy(sizePolicy)
        self.spinBoxTime.setMaximumSize(QtCore.QSize(60, 16777215))
        self.spinBoxTime.setObjectName(_fromUtf8("spinBoxTime"))
        self.gridLayout.addWidget(self.spinBoxTime, 1, 2, 1, 1)
        self.lineEditTitle = QtGui.QLineEdit(self.groupBoxMessages)
        self.lineEditTitle.setObjectName(_fromUtf8("lineEditTitle"))
        self.gridLayout.addWidget(self.lineEditTitle, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBoxMessages)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.ShowButton = QtGui.QPushButton(self.groupBoxMessages)
        self.ShowButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.ShowButton.setObjectName(_fromUtf8("ShowButton"))
        self.gridLayout.addWidget(self.ShowButton, 4, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxMessages)

        self.retranslateUi(TrayIcon)
        QtCore.QMetaObject.connectSlotsByName(TrayIcon)

    def retranslateUi(self, TrayIcon):
        TrayIcon.setWindowTitle(_translate("TrayIcon", "Form", None))
        self.groupBoxTrayIcon.setTitle(_translate("TrayIcon", "托盘图标", None))
        self.label.setText(_translate("TrayIcon", "图标： ", None))
        self.checkBoxShowIcon.setText(_translate("TrayIcon", "展示图标", None))
        self.checkBoxQQmsg.setText(_translate("TrayIcon", "QQ消息效果", None))
        self.groupBoxMessages.setTitle(_translate("TrayIcon", "气泡消息", None))
        self.label_5.setText(_translate("TrayIcon", "标题： ", None))
        self.label_3.setText(_translate("TrayIcon", "持续时长： ", None))
        self.label_2.setText(_translate("TrayIcon", "类型： ", None))
        self.label_6.setText(_translate("TrayIcon", "内容： ", None))
        self.ShowButton.setText(_translate("TrayIcon", "展示消息", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    TrayIcon = QtGui.QWidget()
    ui = Ui_TrayIcon()
    ui.setupUi(TrayIcon)
    TrayIcon.show()
    sys.exit(app.exec_())
