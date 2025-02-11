import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import QDateTime
from ui_main import Ui_ToDoApp
from new_todo import Ui_Dialog
from connection import Data
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

API_TOKEN = '7631067443:AAFn13qh1KQFDUjP3Zk5h_6HujgWLlzovFw'
CHAT_ID = '963156876'  # Идентификатор чата, куда будут отправляться сообщения

# Создаём бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

todos_time = []



# Подкласс QMainWindow для настройки основного окна приложения
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
        self.ui_window.dateTimeEdit.setDateTime(QDateTime.fromString(self.conn.get_smth_todo_query(3, id), "M/d/yy h:mm A"))




async def send_message():
    # Функция для отправки сообщения
    await bot.send_message(CHAT_ID, "Наступило нужное время!")


async def check_time_and_send():
    while True:
        current_time = QDateTime.currentDateTime()
        if current_time:
            await send_message()  # Отправляем сообщение в Telegram
            await asyncio.sleep(60)  # Ждём 60 секунд, чтобы не отправлять несколько сообщений за раз
        await asyncio.sleep(1)  # Периодически проверяем время


async def main():
    # Запуск бота в фоновом режиме
    bot_task = asyncio.create_task(dp.start_polling())

    # Запуск проверки времени
    time_task = asyncio.create_task(check_time_and_send())

    # Ожидание обоих процессов
    await asyncio.gather(bot_task, time_task)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    for i in [QDateTime.fromString(j, "M/d/yy h:mm A") for j in window.conn.get_smth_all_todo_query(3)]:
        todos_time.append(i)
    print(todos_time)
    sys.exit(app.exec())
    asyncio.run(main)
