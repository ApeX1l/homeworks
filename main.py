import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.addButton.clicked.connect(self.add)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('coffe_name')
        model.select()

        self.view.setModel(model)
        self.view.move(90, 230)
        self.view.resize(617, 315)

    def add(self):
        sqlite_connection = sqlite3.connect('coffee.sqlite')
        cursor = sqlite_connection.cursor()
        cursor.execute('INSERT INTO coffe_name(name_of_sort) VALUES ("")')
        sqlite_connection.commit()
        cursor.close()
        try:
            self.initUI()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
