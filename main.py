import sys
from datetime import datetime
# from PySide6 import QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_ToDoApp


# Подкласс QMainWindow для настройки основного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ToDoApp()
        self.ui.setupUi(self)


    # def date_time_response(self):
    #     if self.datetime.dateTime() == QDateTime.currentDateTime():
    #         self.userdate = self.datetime.dateTime()
    #
    # def message_set(self):
    #     self.message = self.usertext.text



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
    # app.setStyleSheet(StyleSheet)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
