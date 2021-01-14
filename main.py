from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPlainTextEdit
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

    def addHolders(self):
        qptRecieved = QPlainTextEdit(self)
        qptRecieved.move(10, 30)
        qptRecieved.resize(480, 320)
        qptRecieved.setReadOnly(True)
        self.qptRecieved = qptRecieved

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cc = MainWindow()
    cc.show()
    sys.exit(app.exec_())