import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'UI.ui', self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.painted = False

    def paintEvent(self, event):
        if self.painted:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            for i in range(7):
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
