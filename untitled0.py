# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:37:17 2021

@author: Administrator
"""

import sys

#from PyQT5.QtWidgets import QApplication,QWidget

#from ui_Widget import Ui_Widget
#class QmyWidget(QWidget):
#    def __init__(self,parent=None):
#        super().__init__(parent)
#        self.ui=Ui_Widget()
#        self.ui.setupUi(self)
    


from PyQt5.QtWidgets import QApplication,QMainWindow

from ui_MainWindow import Ui_MainWindow
class QmyMainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


if __name__=="__main__":
    app=QApplication(sys.argv)
    form=QmyMainWindow()
    form.show()
    sys.exit(app.exec_())