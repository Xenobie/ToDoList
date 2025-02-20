import sys
import asyncio
from main import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QDateTime
from aiogram import Bot, Dispatcher


app = QApplication(sys.argv)

window = MainWindow()

API_TOKEN = '7631067443:AAFn13qh1KQFDUjP3Zk5h_6HujgWLlzovFw'
CHAT_ID = '963156876'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def check_time_loop():
    tasks_ids = window.conn.get_id_todo_query()
    while True:
        for i in tasks_ids:
            query_result = window.conn.get_smth_todo_query(3, i)
            query_title_result = window.conn.get_smth_todo_query(1, i)

            if query_result is None:
                print("Ошибка: база данных вернула None!")
                await asyncio.sleep(10)
                continue

            target_time = QDateTime.fromString(query_result, "dd.MM.yyyy HH:mm")

            if not target_time.isValid():
                print(f"Ошибка: не удалось распознать дату из '{query_result}'")
                target_time = QDateTime.fromString(query_result, "M/d/yy h:mm A")
                await asyncio.sleep(10)

            current_time = QDateTime.currentDateTime()
            if current_time >= target_time:
                await bot.send_message(CHAT_ID, f"Наступило нужное время! Для задачи {query_title_result}")
                tasks_ids.remove(i)
                break
            await asyncio.sleep(1)

async def mainBot():
    try:
        await asyncio.create_task(check_time_loop())
    finally:
        await bot.session.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(mainBot())

