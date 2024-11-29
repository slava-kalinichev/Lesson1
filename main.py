import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton, QMessageBox

# Тест github
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.labels = []
        self.line_edits = []
        teams = ["First name", "Middle name", "Last name", "DocType", "DocNumber"]
        y_offset = 20
        for i in range(len(teams)):
            team = teams[i]
            label = QLabel(f'{team}:', self)
            label.move(20, y_offset)
            if i in (0, 1, 2):
                line_edit = QLineEdit(self)
                line_edit.move(120, y_offset)
                self.labels.append(label)
                self.line_edits.append(line_edit)
            elif i == 3:
                combo_box = QComboBox(self)
                combo_box.addItems(["RuPass", "RuDL", "RuForeignPass", "InterPass", "InterDL"])
                combo_box.move(120, y_offset)
                line_edit = combo_box.currentText()
                self.labels.append(label)
                self.line_edits.append(line_edit)
            elif i == 4:
                line_edit = QLineEdit(self)
                line_edit.move(120, y_offset)
                self.labels.append(label)
                self.line_edits.append(f'{line_edit.text()[0:4:]} {line_edit.text()[4:]}')
            y_offset += 50

        self.find_button = QPushButton('Find', self)
        self.find_button.move(80, y_offset)
        self.find_button.clicked.connect(self.on_find_clicked)
        self.setWindowTitle('LoanBase')

    def on_find_clicked(self):
        values = [line_edit.text() for line_edit in self.line_edits]
        QMessageBox.information(self, 'Values', '\n'.join(values))

        self.setWindowTitle('PyQt6 Example')

    def on_find_clicked(self):
        values = [line_edit.text() for line_edit in self.line_edits]
        QMessageBox.information(self, 'Values', '\n'.join(values))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
