from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPlainTextEdit, QLineEdit, QPushButton
from PyQt5.QtNetwork import QTcpSocket
import json
import sys

class MainWindow(QMainWindow):
    SERVER = '10.242.242.216'
    PORT = 7778
    FORMAT = 'utf-8'
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatClient")
        self.setFixedSize(500, 500)

        self.addLabels()
        self.addHolders()
        self.addSocket()
        self.addButtons()

    def showMessage(self, msg):
        message = "[{name}] {msg}".format(
            name=msg["name"],
            msg=msg["msg"]
        )
        log = "{history}\n{msg}".format(
            history=self.qptRecieved.toPlainText(),
            msg=message
        )
        self.qptRecieved.setPlainText(log)

    def showCount(self, msg):
        self.lblCount.setText("Connected users: {count}".format(
            count=msg["count"]
        ))
        pass

    def formatMsg(self, reading)->dict:
        msg = bytes(reading).decode(MainWindow.FORMAT)
        try:
            return json.loads(msg)
        except:
            return {}

    def formatJson(self, **kwargs)->bytes:
        data = {}
        for key, val in kwargs.items():
            data[key] = val
        return json.dumps(data).encode(MainWindow.FORMAT)

    def addSocket(self):
        socket = QTcpSocket(self)
        def onConnect():
            print("[CLIENT CONNECTED]")

        def onDisconnect():
            print("[CLIENT DISCONNECTED]")

        def onRead():
            msg = self.formatMsg(socket.readAll())

            switcher = {
                "msg": self.showMessage,
                "count": self.showCount
            }
            
            func = switcher.get(msg["type"], lambda x:print(x))
            func(msg)

        socket.connected.connect(onConnect)
        socket.disconnected.connect(onDisconnect)
        socket.readyRead.connect(onRead)
        self.socket = socket
        socket.connectToHost(MainWindow.SERVER, MainWindow.PORT)

    def addLabels(self):
        lblRecieved = QLabel(self)
        lblRecieved.move(10, 10)
        lblRecieved.resize(100, 15)
        lblRecieved.setText("Messages recieved:")

        lblCount = QLabel(self)
        lblCount.move(250, 10)
        lblCount.resize(100, 15)
        self.lblCount = lblCount

        lblName = QLabel(self)
        lblName.move(10, 357)
        lblName.resize(35, 15)
        lblName.setText("Name:")

    def addHolders(self):
        qptRecieved = QPlainTextEdit(self)
        qptRecieved.move(10, 30)
        qptRecieved.resize(480, 320)
        qptRecieved.setReadOnly(True)
        self.qptRecieved = qptRecieved

        qleName = QLineEdit(self)
        qleName.move(45, 355)
        qleName.resize(315, 20)
        qleName.setMaxLength(50)
        self.qleName = qleName

        qptMessage = QPlainTextEdit(self)
        qptMessage.move(10, 380)
        qptMessage.resize(350, 110)

        def sizeChecker():
            txt = qptMessage.toPlainText()
            if(len(txt) > 500):
                qptMessage.setPlainText(txt[1::])
            pass
        qptMessage.textChanged.connect(sizeChecker)
        self.qptMessage = qptMessage

    def addButtons(self):
        btnClear = QPushButton(self)
        btnClear.move(370, 355)
        btnClear.resize(120, 60)
        btnClear.setText("Clear Chat")
        def clearChat():
            self.qptRecieved.setPlainText("")
        btnClear.clicked.connect(clearChat)

        btnSend = QPushButton(self)
        btnSend.move(370, 430)
        btnSend.resize(120, 60)
        def sendMsg():
            if(self.socket.state() == QTcpSocket.ConnectedState):
                name = self.qleName.text()
                msg = self.qptMessage.toPlainText()

                self.qptMessage.setPlainText("")
                self.qptMessage.setFocus()
                self.socket.writeData(self.formatJson(
                    name=name,
                    msg=msg,
                    type="msg"
                ))
        btnSend.setText("Send Message")
        btnSend.clicked.connect(sendMsg)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    cc = MainWindow()
    cc.show()
    sys.exit(app.exec_())