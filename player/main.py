# -*- coding: UTF8 -*-
import os
import win32api

import mp3play
import win32con
from PyQt4 import QtCore, QtGui

from player import Ui_TrayIcon


# import icoqrc


class mainTray(QtGui.QWidget, Ui_TrayIcon):
    def __init__(self):
        super(mainTray, self).__init__()
        # self.Ui= Ui_TrayIcon()
        self.setupUi(self)
        self.setWindowTitle(u'Pyqt 托盘效果')
        self.setWindowIcon(QtGui.QIcon('tuopan.ico'))
        self.setFixedSize(590, 106)
        self.play = False
        self.PowerBoot = False
        self.flag = False
        # 填充Ui内容
        self.supplyUi()
        # 创建icon
        self.createTrayIcon()

        # 通知区域icon显示
        self.trayIcon.activated.connect(self.iconActivated)  # 触发托盘事件
        # self.Ui.checkBoxShowIcon.toggled.connect(self.trayIcon.setVisible)  # 触发是否显示托盘图标
        self.trayIcon.show()  # 托盘show
        # self.Ui.ShowButton.clicked.connect(self.showMessage)   # 触发展示消息
        # self.trayIcon.messageClicked.connect(self.messageClicked)   # 点击提示消息
        # self.threadTask()  # 线程任务

    def supplyUi(self):
        # 设置 标题和提示的初始化内容
        while True:
            try:
                with open(r"Conf.ini", "r") as Conf:
                    Conf = Conf.readlines()
                    if Conf[0].split()[0] == "None":
                        self.lineEditTitle.setText(u"等待添加音频")
                    else:
                        self.lineEditTitle.setText(Conf[0])
                    if Conf[1]:
                        self.kaijiqidong.setChecked(True)
                    else:
                        self.kaijiqidong.setChecked(False)
                    break
            except IOError:
                with open(r"Conf.ini", "w") as Conf:
                    Conf.write("None")
                    Conf.write("\n%s" % self.PowerBoot)
            except IndexError:
                with open(r"Conf.ini", "w") as Conf:
                    Conf.write("None")
                    Conf.write("\n%s" % self.PowerBoot)

    # 创建icon 与菜单
    def createTrayIcon(self):
        # 设置icon
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
        # 设置icon
        self.trayIcon.setIcon(QtGui.QIcon('tuopan.ico'))

    # 触发托盘icon
    def iconActivated(self, reason):
        if reason in (QtGui.QSystemTrayIcon.Trigger, QtGui.QSystemTrayIcon.DoubleClick):
            self.showNormal()

    def open_path(self):
        self.source_path = unicode(QtGui.QFileDialog.getOpenFileName(self))
        self.lineEditTitle.setText(self.source_path)
        with open(r"Conf.ini", "w") as Conf:
            Conf.write(self.source_path)
            Conf.write("\n%s" % self.PowerBoot)

    def start(self):
        if self.lineEditTitle.text() != u"等待添加音频":
            self.source_path = self.lineEditTitle.text()
        elif self.lineEditTitle.text() == "":
            self.open_path()

        if self.play == False:
            try:
                self.mp3 = mp3play.load(self.source_path)
                self.startmp3.setText(u"停止")

            except:
                QtGui.QMessageBox.warning(self, u'确认', u'音频播放错误或路径内不能含有中文，请重新确认', QtGui.QMessageBox.Ok)

            self.mp3.play()
            self.play = True
        else:
            self.startmp3.setText(u"开始")
            self.mp3.stop()
            self.play = False

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.hide()

    def addfile2autorun(self, path):
        runpath = "Software\Microsoft\Windows\CurrentVersion\Run"
        hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_SET_VALUE)
        path = os.path.abspath(path)
        if False == os.path.isfile(path):
            return False
        (filepath, filename) = os.path.split(path)
        win32api.RegSetValueEx(hKey, filename, 0, win32con.REG_SZ, path)
        win32api.RegCloseKey(hKey)
        return True

    def delfile2autorun(self, path):
        runpath = "Software\Microsoft\Windows\CurrentVersion\Run"
        hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_SET_VALUE)
        win32api.RegCreateKey(hKey, 'Python')
        path = os.path.abspath(path)
        if False == os.path.isfile(path):
            return False
        (filepath, filename) = os.path.split(path)
        win32api.RegDeleteValue(hKey, filename)
        win32api.RegCloseKey(hKey)
        return True

    def kaiji(self):
        if self.lineEditTitle.text() != u"等待添加音频":
            self.source_path = self.lineEditTitle.text()
        else:
            self.source_path = "None"
        if self.kaijiqidong.isChecked():
            path = sys.argv[0]
            if self.addfile2autorun(path):
                self.PowerBoot = True
                with open(r"Conf.ini", "w") as Conf:
                    Conf.write(self.source_path)
                    Conf.write("\n%s" % self.PowerBoot)
        else:
            path = sys.argv[0]
            if self.delfile2autorun(path):
                self.PowerBoot = False
                with open(r"Conf.ini", "w") as Conf:
                    Conf.write(self.source_path)
                    Conf.write("\n%s" % self.PowerBoot)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    # QtGui.QApplication.setQuitOnLastWindowClosed(False)
    trany = mainTray()
    trany.show()
    sys.exit(app.exec_())
