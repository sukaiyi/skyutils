from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QRect

class TransQComboBox(QComboBox):
	def __init__(self,items,icons):
		super().__init__()
		self.items = items
		self.icons = icons
		self.initUI()

	def initUI(self):
		self.setView(QListView())
		for item in self.items:
			self.addItem(QIcon(self.icons[item['value']]),item['key'])

class TitleWidget(QWidget):
	def __init__(self,title):
		super().__init__()
		self.setObjectName('TitleWidget')
		self.title = title
		self.initUI()

	def initUI(self):
		self.titleLabel = QLabel(self.title)
		self.titleLabel.setObjectName('titleLabel')
		self.iconLabel = QPushButton()
		self.iconLabel.setObjectName('iconLabel')

		hbox = QHBoxLayout()
		hbox.addWidget(self.iconLabel)
		hbox.addWidget(self.titleLabel)
		hbox.addStretch(1)

		self.setLayout(hbox)