import sys
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Name")
        hLayout = QHBoxLayout()
        hLayout.addWidget(QPushButton("First Button"))
        hLayout.addWidget(QPushButton("Second Button"))
        hLayout.addWidget(QPushButton("Third Button"))
        self.setLayout(hLayout)
        print(self.children())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= Window()
    window.show()
    sys.exit(app.exec_())
    