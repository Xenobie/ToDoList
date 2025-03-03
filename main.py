import sys
import asyncio
import logging
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import QDateTime, QThread
from ui_main import Ui_ToDoApp
from new_todo import Ui_Dialog
from connection import Data
from aiogram import Bot, Dispatcher

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
        self.ui_window.dateTimeEdit.setDateTime(QDateTime.fromString(self.conn.get_smth_todo_query(3, id), "dd.MM.yyyy HH:mm"))

app = QApplication(sys.argv)
window = MainWindow()

# ----------- TELEГРАМ БОТ ----------- #
API_TOKEN = '7631067443:AAFn13qh1KQFDUjP3Zk5h_6HujgWLlzovFw'
CHAT_ID = '963156876'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def check_time_loop():
    logging.debug("Фоновый процесс запущен!")
    while True:
        tasks_ids = window.conn.get_id_todo_query()
        logging.debug(f"Получены ID задач: {tasks_ids}")

        for i in tasks_ids:
            query_result = window.conn.get_smth_todo_query(3, i)
            query_title_result = window.conn.get_smth_todo_query(1, i)

            if query_result is None:
                logging.warning("Ошибка: база данных вернула None!")
                await asyncio.sleep(10)
                continue

            target_time = QDateTime.fromString(query_result, "dd.MM.yyyy HH:mm")

            if not target_time.isValid():
                logging.warning(f"Ошибка: не удалось распознать дату из '{query_result}'")
                target_time = QDateTime.fromString(query_result, "M/d/yy h:mm A")
                await asyncio.sleep(10)

            current_time = QDateTime.currentDateTime()
            logging.debug(f"Текущая дата: {current_time}, задача: {query_title_result}, запланировано: {target_time}")

            if current_time >= target_time:
                logging.info(f"Отправка уведомления: {query_title_result}")
                await bot.send_message(CHAT_ID, f"Наступило нужное время! Для задачи {query_title_result}")
                tasks_ids.remove(i)
                break
        await asyncio.sleep(1)

async def mainBot():
    logging.info("Запуск бота и проверки времени...")
    asyncio.create_task(check_time_loop())  # Запускаем проверку времени в фоне
    await dp.start_polling(bot)  # Используем start_polling вместо run_polling

class BotThread(QThread):
    def __init__(self):
        super().__init__()
        self.loop = None

    def run(self):
        logging.info("Запуск потока бота...")
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(mainBot())

if __name__ == "__main__":
    logging.info("Запуск GUI...")
    window.show()

    bot_thread = BotThread()
    bot_thread.start()  # Запускаем поток с ботом

    sys.exit(app.exec())
