from PyQt5.QtWidgets import QWidget,QListView,QListWidget,QListWidgetItem,QGraphicsDropShadowEffect,QLabel,QStackedLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,QSize,QEvent,QCoreApplication,QPropertyAnimation

import math

from configuration import Items

class FadeWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.installEventFilter(self)

	def eventFilter(self,object,event):
		if event.type() == QEvent.WindowDeactivate:
			self.halfHide()
		elif event.type() == QEvent.WindowActivate:
			self.recoverHalfHide()
		return super().eventFilter(object,event)

	def halfHide(self):
		if self.windowOpacity() < 0.05:
			return None
		self.animation = QPropertyAnimation(self,   b'windowOpacity')
		self.animation.setDuration(100)
		self.animation.setStartValue(1)
		self.animation.setEndValue(0.5)
		self.animation.start()

	def recoverHalfHide(self):
		if self.windowOpacity() > 0.95:
			return None
		self.animation = QPropertyAnimation(self,   b'windowOpacity')
		self.animation.setDuration(100)
		self.animation.setStartValue(self.windowOpacity())
		self.animation.setEndValue(1)
		self.animation.start()

	def hide(self):
		self.animation = QPropertyAnimation(self,   b'windowOpacity')
		self.animation.setDuration(200)
		self.animation.setStartValue(1)
		self.animation.setEndValue(0)
		self.animation.finished.connect(super().hide)
		self.animation.start()

	def show(self):
		super().show()
		self.animation = QPropertyAnimation(self,   b'windowOpacity')
		self.animation.setDuration(200)
		self.animation.setStartValue(0)
		self.animation.setEndValue(1)
		self.animation.start()

class ActionListWidget(QListWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setViewMode(QListView.IconMode);
		for item in Items:
			widgetItem = QListWidgetItem(self)
			widgetItem.setText(item['title'])
			widgetItem.setToolTip(item['description'] if 'description' in item.keys() else '')
			widgetItem.setIcon(QIcon(item['icon']))
			self.addItem(widgetItem)
		self.setIconSize(QSize(48,48))
		self.setMovement(QListView.Static)
		self.setUniformItemSizes(True)

		self.setSize()

		shadow = QGraphicsDropShadowEffect(self)
		shadow.setColor(Qt.black);
		shadow.setBlurRadius(10)
		shadow.setOffset(0,0)
		self.setGraphicsEffect(shadow)

	def setSize(self):
		itemNum = len(Items)
		rows = math.ceil(itemNum/10)
		cols = itemNum if rows == 1 else 10
		self.setMaximumSize(40 + cols * 75, rows * 80)
		self.setMinimumSize(40 + cols * 75, rows * 80)

	def mousePressEvent(self,event):
		self.moved = False
		self.mouseInWindowPos = event.globalPos() - self.parentWidget().pos()
		return super().mousePressEvent(event)

	def mouseMoveEvent(self,event):
		r = super().mouseMoveEvent(event)
		self.moved = True
		windPos = event.globalPos() - self.mouseInWindowPos
		self.parentWidget().move(windPos)
		return r

	def mouseReleaseEvent(self,event):
		if not self.moved:
			return super().mouseReleaseEvent(event)
		
		
class ResultPanel(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.messageLabel = QLabel()
		self.messageLabel.setObjectName('messageLabel')
		self.messageLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
		self.messageLabel.setWordWrap(True)
		self.messageLabel.setScaledContents(True)
		self.messageLabel.setAlignment(Qt.AlignTop)

		self.iconLabel = QLabel()
		self.iconLabel.setAttribute(Qt.WA_TransparentForMouseEvents,True)
		self.iconLabel.setAlignment(Qt.AlignRight)

		self.layout = QStackedLayout(self)
		self.layout.setStackingMode(QStackedLayout.StackAll)
		self.layout.addWidget(self.iconLabel)
		self.layout.addWidget(self.messageLabel)
		self.setLayout(self.layout)

		shadow = QGraphicsDropShadowEffect(self)
		shadow.setColor(Qt.black);
		shadow.setBlurRadius(10)
		shadow.setOffset(0,0)
		self.setGraphicsEffect(shadow)
		self.hide()

