from GUI.InterfazGrafica import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
"""
Main
"""
def main():
	app = QtGui.QApplication(sys.argv)
	mainWindow = LoginWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()