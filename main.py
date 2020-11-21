import random

from PyQt5 import uic
import sys
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QApplication
from random import choices, choice


class CirclesDrawer(QWidget):
    def __init(self):
        super().__init__()
        uic.loadUi('UI.ui')
        self.pushButton.clicked.connect(self.lets_draw)
        self.drawer = QPainter

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CirclesDrawer()
    ex.show()
    sys.exit(app.exec_())
