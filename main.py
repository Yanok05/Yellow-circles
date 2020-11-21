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

    def lets_draw(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        for i in range(choice(numbers)):
            self.drawer.drawEllipse()

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CirclesDrawer()
    ex.show()
    sys.exit(app.exec_())
