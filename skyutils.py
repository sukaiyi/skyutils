from PyQt5.QtWidgets import QDesktopWidget, QVBoxLayout
import sys

from style import *
from views import *
from application import SingleApplication
import function


class Window(FadeWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.actionList = ActionListWidget()
        self.actionList.itemDoubleClicked.connect(self.itemDoubleClicked)
        self.actionList.itemClicked.connect(self.itemClicked)

        self.resultPanel = ResultPanel()
        layout = QVBoxLayout()
        layout.addWidget(self.actionList)
        layout.addWidget(self.resultPanel)

        self.setLayout(layout)

        self.position()
        self.setStyleSheet(BaseStyle)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.X11BypassWindowManagerHint)
        self.show()
        self.hide()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.X11BypassWindowManagerHint | Qt.WindowStaysOnTopHint)
        self.show()

    def position(self):
        if len(sys.argv) >= 3:
            self.move(int(sys.argv[1]), int(sys.argv[2]))
        else:
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

    def itemDoubleClicked(self, item):
        self.resultPanel.iconLabel.setPixmap(item.icon().pixmap(48, 48))
        function.do(item.text(), self.success, self.failed)

    def itemClicked(self, item):
        if item.text() == 'quit':
            QCoreApplication.quit()
        if item.text() == 'hide':
            self.hide()

    def showResult(self, message, style):
        if not message:
            self.resultPanel.setVisible(False)
            self.adjustSize()
            return
        if len(message) >= 800:
            text = message[:800] + '\n...\ntotal:' + str(len(message))
        else:
            text = message
        self.resultPanel.setVisible(True)
        self.resultPanel.setStyleSheet(style)
        self.resultPanel.messageLabel.setText(text)
        self.adjustSize()

    def success(self, message):
        self.showResult(message, ResultLabelSuccessStyle)

    def failed(self, message):
        self.showResult(message, ResultLabelFailedStyle)


if __name__ == '__main__':
    app = SingleApplication(sys.argv)
    if not app.isRuning:
        win = Window()
        app.mainWindow = win
        sys.exit(app.exec_())
