import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Title")
        vBoxLayout = QVBoxLayout()
        
        vBoxLayout.addWidget(QPushButton("first button"))
        vBoxLayout.addWidget(QPushButton("secone button"))
        vBoxLayout.addWidget(QPushButton("third button"))
        
        self.setLayout(vBoxLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())