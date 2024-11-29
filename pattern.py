from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
import sys


class My_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # main code
        self.button = QPushButton("Name", self)
        self.button.clicked.connect(self.click_button)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button)
        vbox = QVBoxLayout
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle('Название')


    def click_button(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_window()
    window.show()
    sys.exit(app.exec())


