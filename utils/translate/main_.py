from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtWidgets import QWidget,QFrame,QDesktopWidget,QVBoxLayout,QLabel,QGraphicsDropShadowEffect

import utils.translate.style
from views import *

import time


class TransThread(QThread):
	trigger = pyqtSignal()
	def __int__(self):
		super().__init__()
		self.trigger.connect(self.finished)

	def run(self):
		time.sleep(4)
		self.transResult = self.transText + 'ABC'
		self.trigger.emit()

	def finished(self):
		self.success(self.transResult)

class TransWindow(FadeWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		
		layout = QVBoxLayout()
		layout.addWidget(QLabel('hello world'))

		rootWidget = QFrame()
		rootWidget.setLayout(layout)
		rootWidget.setObjectName("rootWidget")
		shadow = QGraphicsDropShadowEffect(self)
		shadow.setColor(Qt.black);
		shadow.setBlurRadius(10)
		shadow.setOffset(0,0)
		rootWidget.setGraphicsEffect(shadow)

		rootLayout = QVBoxLayout()
		rootLayout.addWidget(rootWidget)
		self.setLayout(rootLayout)
		self.setStyleSheet(utils.translate.style.Style)
		self.resize(200,200)

window = None

def translate(transText,success,failed):
	global window
	if window == None:
		window = TransWindow()
	window.show()