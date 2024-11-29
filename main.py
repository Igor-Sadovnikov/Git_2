from random import randint
import sys
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt6 import uic  # Импортируем uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False  
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellyps(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_ellyps(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(1, 100)
        qp.drawEllipse(10, 100, x, x)
        x = randint(1, 100)
        qp.drawEllipse(300, 100, x, x)
        x = randint(1, 100)
        qp.drawEllipse(500, 100, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())