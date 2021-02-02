import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidgetWindow(QWidget):
    def __init__(self):
        super(MyWidgetWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.btn_clicked)

        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def btn_clicked(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        r = random.randint(1, min(self.height(), self.width()) // 2)
        x, y = random.randint(r, self.width() - r), \
               random.randint(r, self.height() - r)

        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidgetWindow()
    ex.show()
    sys.exit(app.exec())
