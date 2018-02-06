from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QEvent, QPointF
from PyQt5.QtNetwork import QLocalServer, QLocalSocket, QAbstractSocket


class SingleApplication(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.TIME_OUT = 1000
        self.isRuning = False
        self.serverName = 'skyutils'
        self.args = args
        self.mousePos = QPointF(0, 0)
        self.initLocalConnection()

    def initLocalConnection(self):
        socket = QLocalSocket()
        socket.connectToServer(self.serverName)
        if socket.waitForConnected(self.TIME_OUT):
            self.isRuning = True
            if len(self.args) >= 3:
                data = self.args[1] + ',' + self.args[2]
                socket.writeData(data.encode())
                socket.flush()
                socket.waitForBytesWritten()
            return
        self.newLocalServer()

    def newLocalServer(self):
        self.localServer = QLocalServer(self)
        self.localServer.newConnection.connect(self.newLocalConnection)
        if not self.localServer.listen(self.serverName):
            if self.localServer.serverError() == QAbstractSocket.AddressInUseError:
                QLocalServer.removeServer(self.serverName)
                self.localServer.listen(self.serverName)

    def newLocalConnection(self):
        socket = self.localServer.nextPendingConnection()
        socket.readyRead.connect(self.readyRead)

    def readyRead(self):
        socket = self.sender()
        if socket:
            data = socket.readData(1000)
            socket.close()
            if data:
                data = data.decode().split(',')
                x, y = 0, 0
                if self.mousePos:
                    x = self.mousePos.x()
                    y = self.mousePos.y()
                self.mainWindow.move(int(data[0]) - x, int(data[1]) - y)
        self.mainWindow.setWindowFlags(self.mainWindow.windowFlags() | Qt.WindowStaysOnTopHint)
        self.mainWindow.show()

    def notify(self, receiver, event):
        if event.type() == QEvent.MouseButtonPress:
            self.mousePos = event.localPos()
        return super().notify(receiver, event)
