import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

#Text

from ViewControllerText import MainWindow
window = MainWindow()

while True:
    print("To add a note press 1. To delete a note press 0. Press 2 to complete a task. To print all the notes press 3. To exit press 4.")
    entry = int(input())
    if entry == 1:
        print("Enter a note to add:")
        window.add(input())
    elif entry == 0:
        print("Enter a note index to delete:")
        window.delete(int(input()))
    elif entry == 2:
        print("Enter a note index to complete:")
        window.complete(int(input()))
    elif entry == 3:
        window.show()
    else:
        break

#GUI

from ViewController import MainWindow
# app = QtWidgets.QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec_()