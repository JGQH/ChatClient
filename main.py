from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cc = MainWindow()
    cc.show()
    sys.exit(app.exec_())