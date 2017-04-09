import os
import sys
import win32api

import win32con


def addfile2autorun(path):
    runpath = "Software\Microsoft\Windows\CurrentVersion\Run"
    hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_SET_VALUE)
    print hKey
    path = os.path.abspath(path)
    if False == os.path.isfile(path):
        return False
    (filepath, filename) = os.path.split(path)
    print filename
    # self.fileHandle = None
    # self.HKEY_CLASSES_ROOT = win32con.HKEY_CLASSES_ROOT
    # self.HKEY_CURRENT_USER = win32con.HKEY_CURRENT_USER
    # self.HKEY_LOCAL_MACHINE = win32con.HKEY_LOCAL_MACHINE
    # self.HKEY_USERS = win32con.HKEY_USERS
    # self.FILE_PATH = "//masblrfs06/karcherarea$/workarea/nishitg/" + win32api.GetComputerName()
    # self.CONST_OS_SUBKEY = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion"
    # self.CONST_PROC_SUBKEY = "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0"
    # self.CONST_SW_SUBKEY = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall"
    # hHandle = win32api.RegOpenKeyEx(self.HKEY_LOCAL_MACHINE, self.CONST_PROC_SUBKEY, 0, win32con.KEY_ALL_ACCESS)
    # print "\xcf\xb5\xcd\xb3\xd5\xd2\xb2\xbb\xb5\xbd\xd6\xb8\xb6\xa8\xb5\xc4\xce\xc4\xbc\xfe\xa1\xa3".decode("gbk").encode("utf-8")
    # print win32api.RegDeleteValue(hKey, "ADKILLER")
    win32api.RegCloseKey(hKey)
    return True


path = sys.argv[0]
addfile2autorun(path)
