from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

from TransViews import *
from config import *
from style import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.fromText = QPlainTextEdit(self)
        self.fromText.textChanged.connect(self.onChanged)
        self.toText = QPlainTextEdit(self)
        self.toText.setReadOnly(True)

        self.fromLanguageBox = TransQComboBox(Config['languages'],Config['icons'])
        self.toLanguageBox = TransQComboBox(Config['languages'],Config['icons'])
        for language in Config['languages']:
            if 'defaultFrom' in language:
                self.fromLanguageBox.setCurrentText(language['key'])
            if 'defaultTo' in language:
                self.toLanguageBox.setCurrentText(language['key'])

        self.switchBtn = QPushButton()
        self.switchBtn.setObjectName('switchBtn')
        self.switchBtn.pressed.connect(self.switchBtnPressed)

        self.titleWidget = TitleWidget('Translate')

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.fromText)
        splitter.addWidget(self.toText)

        hbox = QHBoxLayout()
        hbox.addWidget(self.fromLanguageBox)
        hbox.addStretch(1)
        hbox.addWidget(self.switchBtn)
        hbox.addStretch(1)
        hbox.addWidget(self.toLanguageBox)

        vbox = QVBoxLayout()
        vbox.addWidget(self.titleWidget)
        vbox.addWidget(splitter)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.center()
        self.setStyleSheet(Style)
        self.setWindowTitle('Translate')
        self.show()

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(227, 242, 253)))
        painter.setPen(Qt.transparent)
        rect = self.rect()
        rect.setWidth(rect.width() - 1)
        rect.setHeight(rect.height() - 1)
        painter.drawRoundedRect(rect, 5, 5)
        super().paintEvent(event)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onChanged(self):
        if self.fromText.toPlainText().endswith('\n'):
            pass

    def switchBtnPressed(self):
        fromLanguage = self.fromLanguageBox.currentText()
        toLanguage = self.toLanguageBox.currentText()
        self.fromLanguageBox.setCurrentText(toLanguage)
        self.toLanguageBox.setCurrentText(fromLanguage)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
