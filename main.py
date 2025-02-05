import sys
from datetime import datetime

from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


# Подкласс QMainWindow для настройки основного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QHBoxLayout()

        self.checkbox = QCheckBox()

        self.datetime = QDateTimeEdit()

        self.widget = QLineEdit()
        self.widget.setMaxLength(10)
        self.widget.setPlaceholderText("Enter your text")

        layout.addWidget(self.datetime)
        layout.addWidget(self.widget)
        layout.addWidget(self.checkbox)

        widget = QWidget()
        widget.setLayout(layout)

        # Устанавливаем центральный виджет окна. Виджет будет расширяться по умолчанию,
        # заполняя всё пространство окна.
        self.setCentralWidget(widget)

        self.datetime.dateTimeChanged.connect(self.date_time_response)

    def date_time_response(self):
        print(QDateTime.currentDateTime())
        print(self.datetime.dateTime())
        if self.datetime.dateTime() == QDateTime.currentDateTime():
            print('12354235')

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
