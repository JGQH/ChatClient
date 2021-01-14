from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPlainTextEdit, QLineEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)

        self.addLabels()
        self.addHolders()

    def addLabels(self):
        lblRecieved = QLabel(self)
        lblRecieved.move(10, 10)
        lblRecieved.resize(100, 15)
        lblRecieved.setText("Messages recieved:")

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cc = MainWindow()
    cc.show()
    sys.exit(app.exec_())