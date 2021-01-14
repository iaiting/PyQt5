#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 案例4-2 主窗口居中显示
#
################################################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget


################################################################################
class Winform(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口放在屏幕中间例子')
        self.resize(370, 250)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
