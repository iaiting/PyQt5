#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# 10.1 QTimer
#
################################################################################

import sys
from PyQt5.QtCore import QTimer, Qt

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
)


################################################################################
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.step = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)

        self.ss_button = QPushButton('Start', self)
        self.ss_button.clicked.connect(self.start_stop_func)


        self.v_layout =  QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.ss_button)
        self.setLayout(self.v_layout)

    def start_stop_func(self):
        print('start_stop_func')
        if self.timer.isActive():
            self.timer.stop()
            self.ss_button.setText('Start')
        else:
            self.timer.start(1000)
            self.ss_button.setText('Stop')

    def update_func(self):
        print('update_func')
        self.step += 1
        self.label.setText(str(self.step))
        pass


################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
