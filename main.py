# -*- coding: UTF8 -*-
# UI说明： 新建窗体，添加两个groupbox  右键 -- 布局 -- 垂直布局

import sip

sip.setapi('QVariant', 2)
from PyQt4 import QtCore, QtGui
from ui import Ui_TrayIcon
import threading


# import icoqrc


class mainTray(QtGui.QWidget):
    def __init__(self):
        super(mainTray, self).__init__()
        self.Ui = Ui_TrayIcon()
        self.Ui.setupUi(self)
        self.setWindowTitle(u'Pyqt 托盘效果')
        self.setWindowIcon(QtGui.QIcon('tuopan.ico'))
        # 填充Ui内容
        self.supplyUi()

        # 创建icon
        self.createTrayIcon()

        # 通知区域icon显示
        self.Ui.comboBoxIcon.currentIndexChanged.connect(self.setIcon)  # 链接信号槽
        self.Ui.comboBoxIcon.setCurrentIndex(1)  # 设置当前combox
        self.trayIcon.activated.connect(self.iconActivated)  # 触发托盘事件
        self.Ui.checkBoxShowIcon.toggled.connect(self.trayIcon.setVisible)  # 触发是否显示托盘图标
        self.trayIcon.show()  # 托盘show
        self.Ui.ShowButton.clicked.connect(self.showMessage)  # 触发展示消息
        self.trayIcon.messageClicked.connect(self.messageClicked)  # 点击提示消息
        self.threadTask()  # 线程任务
        self.Ui.checkBoxQQmsg.toggled.connect(self.QQmsg)  # 触发QQ消息效果

    def supplyUi(self):
        # 托盘图标
        self.Ui.comboBoxIcon.addItem(QtGui.QIcon('tuopan.ico'), u'Chrome')
        self.Ui.comboBoxIcon.addItem(QtGui.QIcon(':firefox.ico'), u'Firefox')
        self.Ui.comboBoxIcon.addItem(QtGui.QIcon(':qq.ico'), u'QQ')
        self.Ui.comboBoxIcon.addItem(QtGui.QIcon(':flash.ico'), u'Flash')
        self.Ui.comboBoxIcon.addItem(QtGui.QIcon(':ie.ico'), u'IE')
        self.Ui.comboBoxIcon.addItem(QtGui.QIcon(':myfavicon.ico'), u'Favicon')

        # 默认展示托盘图标
        self.Ui.checkBoxShowIcon.setChecked(True)

        # 消息combox
        self.Ui.comboBox_MsgInfo.addItem("None", QtGui.QSystemTrayIcon.NoIcon)
        self.Ui.comboBox_MsgInfo.addItem(self.style().standardIcon(QtGui.QStyle.SP_MessageBoxInformation), u"信息提示",
                                         QtGui.QSystemTrayIcon.Information)
        self.Ui.comboBox_MsgInfo.addItem(self.style().standardIcon(QtGui.QStyle.SP_MessageBoxWarning), u"警告提示",
                                         QtGui.QSystemTrayIcon.Warning)
        self.Ui.comboBox_MsgInfo.addItem(self.style().standardIcon(QtGui.QStyle.SP_MessageBoxCritical), u"严重警告",
                                         QtGui.QSystemTrayIcon.Critical)

        # 时长显示
        self.Ui.spinBoxTime.setRange(5, 60)  # spinbox 在5--60 之间
        self.Ui.spinBoxTime.setSuffix(" s")  # 设置后缀  s  秒
        self.Ui.spinBoxTime.setValue(15)  # 默认值为15秒

        # 设置 标题和提示的初始化内容
        self.Ui.lineEditTitle.setText(u'无法连接到网络')
        self.Ui.textEditContent.setText(u'您的电脑无法连接到网络，请确保已经接入Internet，or WLAN 端口已经插好！ 有问题请致电：<b>1389876543</b>')

    #  创建icon 与菜单
    def createTrayIcon(self):
        self.minimizeAction = QtGui.QAction(u"最小化", self, triggered=self.hide)
        self.maximizeAction = QtGui.QAction(u"最大化", self, triggered=self.showMaximized)
        self.restoreAction = QtGui.QAction(u"还原大小", self, triggered=self.showNormal)
        self.quitAction = QtGui.QAction(u"退出", self, triggered=QtGui.qApp.quit)
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()  # 分割行
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

    # 触发托盘icon
    def iconActivated(self, reason):
        if reason in (QtGui.QSystemTrayIcon.Trigger, QtGui.QSystemTrayIcon.DoubleClick):
            self.Ui.comboBoxIcon.setCurrentIndex(
                (self.Ui.comboBoxIcon.currentIndex() + 1) % self.Ui.comboBoxIcon.count())
        elif reason == QtGui.QSystemTrayIcon.MiddleClick:  # 点击鼠标滚动轴事件
            self.showMessage()

    # 设置icon
    def setIcon(self, index):
        icon = self.Ui.comboBoxIcon.itemIcon(index)
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)
        self.trayIcon.setToolTip(self.Ui.comboBoxIcon.itemText(index))

    # 展示消息
    def showMessage(self):
        icon = QtGui.QSystemTrayIcon.MessageIcon(
            self.Ui.comboBox_MsgInfo.itemData(self.Ui.comboBox_MsgInfo.currentIndex()))
        self.trayIcon.showMessage(self.Ui.lineEditTitle.text(), self.Ui.textEditContent.toPlainText(), icon,
                                  self.Ui.spinBoxTime.value() * 1000)

    # 点击消息
    def messageClicked(self):
        QtGui.QMessageBox.information(None, "Systray",
                                      "Sorry, I already gave what help I could.\nMaybe you should try asking a human?")

    # 添加一个线程
    def threadTask(self):
        global t
        t = threading.Timer(6.0, self.showMessage)  # 6秒后执行显示消息
        t.start()

    def QQmsg(self):
        import time
        status = self.Ui.checkBoxQQmsg.isChecked()
        comboxicoIndex = self.Ui.comboBoxIcon.currentIndex()
        icon = self.Ui.comboBoxIcon.itemIcon(comboxicoIndex)
        arrs = 1
        whiles = 1
        if status:
            while whiles <= 6:
                if arrs == 1:
                    time.sleep(0.6)
                    self.trayIcon.setIcon(QtGui.QIcon())
                    arrs = 2
                else:
                    time.sleep(0.6)
                    self.trayIcon.setIcon(icon)
                    arrs = 1
                whiles += 1

        else:
            self.trayIcon.setIcon(icon)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.hide()


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setQuitOnLastWindowClosed(False)
    trany = mainTray()
    trany.show()
    sys.exit(app.exec_())
