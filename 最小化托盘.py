# coding:utf-8
import sys

from PyQt4 import QtGui, QtCore


class DigitalClock(QtGui.QLCDNumber):
    '''数字时钟'''

    ######################################## 构造、析构函数 ###################################
    def __init__(self, parent=None):
        '''构造函数'''
        # 调用父类构造函数
        super(DigitalClock, self).__init__(parent)
        # 设置窗口标记
        self.setWindowFlags(QtCore.Qt.Window)
        # 设置窗口标题
        self.setWindowTitle("Digital Clock")
        # 设置窗口尺寸
        self.resize(150, 60)
        # 设置数字显示风格
        self.setSegmentStyle(QtGui.QLCDNumber.Filled)
        # 声明QTimer变量
        timer = QtCore.QTimer(self)
        # 延时连接槽函数
        timer.timeout.connect(self.showTime)
        # 间隔1秒
        timer.start(1000)
        # 显示时间
        self.showTime()

    ######################################### 命令 ############################################
    def showTime(self):
        '''显示时间'''
        # 得到当前时间
        time = QtCore.QTime.currentTime()
        # 转换成QString
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        # 显示时间
        self.display(text)


class MyWindow(QtGui.QWidget):
    '''自定义窗口类'''

    ######################################### 构造、析构函数 ################################
    def __init__(self, parent=None):
        '''构造函数'''
        # 调用父类构造函数
        super(MyWindow, self).__init__(parent)
        # 设置窗口最小尺寸
        self.setMinimumSize(400, 200)
        # 创建主控件
        bodyWidget = QtGui.QWidget(self)
        # 创建主布局
        mainLayout = QtGui.QHBoxLayout(bodyWidget)
        # 设置间距
        mainLayout.setMargin(100)
        # 创建按钮
        digitalClockButton = QtGui.QPushButton(u"打开数字时钟")
        showOrHideButton = QtGui.QPushButton(u"显示/隐藏")
        # 设置按钮连接槽函数
        digitalClockButton.clicked.connect(self.AddDigitalClock)
        showOrHideButton.clicked.connect(self.showOrHideWindow)
        # 添加按钮
        mainLayout.addWidget(digitalClockButton)
        mainLayout.addWidget(showOrHideButton)

    ######################################### 命令 ############################################
    def AddDigitalClock(self):
        '''添加数字时钟'''
        # 创建电子时钟
        self.m_aDigitalClock = DigitalClock(self)
        # 显示
        self.m_aDigitalClock.show()

    def showOrHideWindow(self):
        '''显示或隐藏窗口'''
        # 判断是否打开数字时钟
        if hasattr(self, 'm_aDigitalClock'):
            # 设置隐藏
            if self.m_aDigitalClock.isVisible():
                self.m_aDigitalClock.setVisible(False)
            # 设置显示
            else:
                self.m_aDigitalClock.setVisible(True)
                # 判断窗口是否有QtCore.Qt.Tool
                if self.m_aDigitalClock.windowType() == QtCore.Qt.Tool:
                    # 设置窗口标记(包含最大化、最小化按钮)
                    self.m_aDigitalClock.setWindowFlags(QtCore.Qt.Window)
                    # 显示
                    self.m_aDigitalClock.show()


app = QtGui.QApplication(sys.argv)
qt = MyWindow()
qt.show()
sys.exit(app.exec_())
