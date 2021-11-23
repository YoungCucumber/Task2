import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Draw(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        QApplication.setStyle('Windows')
        self.btn_draw.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circles(self, qp):
        for i in range(randint(1, 10)):
            qp.setBrush(QColor(255, 255, 0))
            rad = randint(10, 130)
            qp.drawEllipse(randint(0, 588), randint(0, 605), rad, rad)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Draw()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())