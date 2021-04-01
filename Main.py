
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
def window():
    app=QApplication(sys.argv[:])
    win=QMainWindow()
    win.setGeometry(200,200,1200,800)
    win.setWindowTitle("YT Stats and Downloader ")
    label=QtWidgets.Qlabel()
    label.setText("Enter The Path")
    win.show()
    sys.exit(app.exec_())
window()
