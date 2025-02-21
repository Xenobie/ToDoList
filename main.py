import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import QDateTime, QThread
from ui_main import Ui_ToDoApp
from new_todo import Ui_Dialog
from connection import Data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ToDoApp()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.ui.btn_add_todo.clicked.connect(self.open_new_todo_window)
        self.ui.btn_edit_todo.clicked.connect(self.open_new_todo_window)
        self.ui.btn_edit_todo.clicked.connect(self.edit_change_todo_text)
        self.ui.btn_delete_todo.clicked.connect(self.delete_current_todo)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('todos')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def open_new_todo_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        sender = self.sender()
        if sender.text() == "Add":
            self.ui_window.pushButton.clicked.connect(self.add_new_todo)
        else:
            self.ui_window.pushButton.clicked.connect(self.edit_current_todo)

    def add_new_todo(self):
        date = self.ui_window.dateTimeEdit.text()
        title = self.ui_window.lineEdit.text()
        description = self.ui_window.lineEdit_2.text()

        self.conn.add_new_todo_query(title, description, date)
        self.view_data()
        self.new_window.close()

    def edit_current_todo(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        date = self.ui_window.dateTimeEdit.text()
        title = self.ui_window.lineEdit.text()
        description = self.ui_window.lineEdit_2.text()

        self.conn.update_todo_query(title, description, date, id)
        self.view_data()
        self.new_window.close()

    def delete_current_todo(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))
        self.view_data()
        self.conn.delete_todo_query(id)

    def edit_change_todo_text(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))
        self.ui_window.lineEdit.setText(self.conn.get_smth_todo_query(1, id))
        self.ui_window.lineEdit_2.setText(self.conn.get_smth_todo_query(2, id))
        date = QDateTime.fromString(self.conn.get_smth_todo_query(3, id), "dd.MM.yyyy HH:mm")
        if not date.isValid():
            self.ui_window.dateTimeEdit.setDateTime(QDateTime.fromString(self.conn.get_smth_todo_query(3, id), "M/d/yy h:mm A"))
        else:
            self.ui_window.dateTimeEdit.setDateTime(QDateTime.fromString(date))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
