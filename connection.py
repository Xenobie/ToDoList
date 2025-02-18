from PySide6 import QtWidgets, QtSql
from PySide6.QtSql import QSqlDatabase
print(QSqlDatabase.drivers())  # Это выведет список доступных драйверов

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('todos_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open db",
                                           "Click cancel to abort", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS todos (ID integer primary key AUTOINCREMENT, Title VARCHAR(20), "
                   "Description VARCHAR(20), Date VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_todo_query(self, title, description, date):
        sql_query = "INSERT INTO todos (Title, Description, Date) VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [title, description, date])

    def update_todo_query(self, title, description, date, id):
        sql_query = "UPDATE todos SET Title=?, Description=?, Date=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [title, description, date, id])

    def delete_todo_query(self, id):
        sql_query = "DELETE FROM todos WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_smth_todo_query(self, smth, id):
        sql_query = "SELECT * FROM todos WHERE ID=?"
        query = self.execute_query_with_params(sql_query, [id])

        # Проверяем, был ли найден хотя бы один результат
        if query.next():
            # Получаем значение из первой колонки (Title)
            return query.value(smth)  # Возвращает значение из первого столбца
        else:
            # Если запись не найдена, можно вернуть None или пустое значение
            return None

    def get_id_todo_query(self):
        sql_query = "SELECT ID FROM todos"
        query = self.execute_query_with_params(sql_query, [])

        # Проверяем, был ли найден хотя бы один результат
        column_data = []
        if not query.isActive():
            print("❌ SQL-запрос не выполнен!")
            print(f"❌ Ошибка SQL: {query.lastError().text()}")
        while query.next():
            column_data.append(query.value(0))  # Получаем значение из первого столбца запроса

        return column_data
