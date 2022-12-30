import sys
from Ui import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.painted = False

    def paintEvent(self, event):
        if self.painted:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            for i in range(7):
                r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
                qp.setBrush(QColor(r, g, b))
                x, y = randint(30, 600), randint(30, 600)
                radius = randint(30, 200)
                qp.drawEllipse(x, y, radius, radius)
            qp.end()

    def btn_clicked(self):
        self.painted = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
