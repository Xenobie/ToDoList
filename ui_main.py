# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
import res_rc

class Ui_ToDoApp(object):
    def setupUi(self, ToDoApp):
        if not ToDoApp.objectName():
            ToDoApp.setObjectName(u"ToDoApp")
        ToDoApp.resize(856, 590)
        ToDoApp.setStyleSheet(u"background-color: rgb(10, 10, 10);")
        self.centralwidget = QWidget(ToDoApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Agency FB"])
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 50px;\n"
"color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section{\n"
"background-color: rgb(59, 59, 59);\n"
"border: none;\n"
"color: white;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item{\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QtableView::item:select{\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout.addWidget(self.tableView)

        self.btn_add_todo = QPushButton(self.centralwidget)
        self.btn_add_todo.setObjectName(u"btn_add_todo")
        self.btn_add_todo.setStyleSheet(u"QPushButton{color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add_todo.setIcon(icon)

        self.verticalLayout.addWidget(self.btn_add_todo)

        self.btn_edit_todo = QPushButton(self.centralwidget)
        self.btn_edit_todo.setObjectName(u"btn_edit_todo")
        self.btn_edit_todo.setStyleSheet(u"QPushButton{color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_edit_todo.setIcon(icon1)

        self.verticalLayout.addWidget(self.btn_edit_todo)

        self.btn_delete_todo = QPushButton(self.centralwidget)
        self.btn_delete_todo.setObjectName(u"btn_delete_todo")
        self.btn_delete_todo.setStyleSheet(u"QPushButton{color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_todo.setIcon(icon2)

        self.verticalLayout.addWidget(self.btn_delete_todo)

        ToDoApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(ToDoApp)

        QMetaObject.connectSlotsByName(ToDoApp)
    # setupUi

    def retranslateUi(self, ToDoApp):
        ToDoApp.setWindowTitle(QCoreApplication.translate("ToDoApp", u"ToDoApp", None))
        self.label.setText(QCoreApplication.translate("ToDoApp", u"Your ToDo`s", None))
        self.btn_add_todo.setText(QCoreApplication.translate("ToDoApp", u"Add", None))
        self.btn_edit_todo.setText(QCoreApplication.translate("ToDoApp", u"Edit", None))
        self.btn_delete_todo.setText(QCoreApplication.translate("ToDoApp", u"Delete", None))
    # retranslateUi

