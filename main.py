import sys
from datetime import datetime

from PyQt6.QtCore import Qt, QDateTime, QRect
import PySide6.QtGui
from PyQt6.QtWidgets import *


# Подкласс QMainWindow для настройки основного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QHBoxLayout()

        self.checkbox = QCheckBox()

        self.datetime = QDateTimeEdit()
        self.datetime.setFixedWidth(150)

        self.datetime.setStyleSheet("QDateTimeEdit{\n"
                                    ""
                                    ""
                                    ""
                                    "")

        self.usertext = QLineEdit()
        self.usertext.setMaxLength(10)
        self.usertext.setPlaceholderText("Enter your text")

        self.usertext.setStyleSheet("   QLineEdit{\n"
                                      "    border-radius: 10px;\n"
                                      "    font-size: 20px;\n"
                                      "    font-weight: bold;\n"
                                      "    background: white;\n"
                                      "    height: 50px;\n"
                                      "    width: 150px;\n"
                                      "}\n"
                                      "\n"
                                      "    QLineEdit:hover {\n"
                                      "    border: 3px solid rgb(61,181,233);\n"
                                      "    }")
        self.usertext.setGeometry(QRect(180, 240, 340, 50))
        self.usertext.setFixedWidth(150)

        layout.addWidget(self.datetime)
        layout.addWidget(self.usertext)
        layout.addWidget(self.checkbox)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.datetime.dateTimeChanged.connect(self.date_time_response)

    def date_time_response(self):
        if self.datetime.dateTime() == QDateTime.currentDateTime():
            self.userdate = self.datetime.dateTime()

    def message_set(self):
        self.message = self.usertext.text


StyleSheet = '''
QDateEdit{
    background-color: rgb(27, 29, 35);
    border-radius: 5px;
    border: 2px solid rgb(33, 37, 43);
/*    padding: 5px;                                                  <----  ??? */
    padding-left: 10px;
    color: rgb(113, 126, 149)
}
QDateEdit:hover{
    border: 2px solid rgb(64, 71, 88);
}
QDateEdit::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px; 
    border-left-width: 3px;
    border-left-color: rgba(39, 44, 54, 150);
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;    
    background-image: url(cil-arrow-bottom.png);         /* <---- установите свое */
    background-position: center;
    background-repeat: no-reperat;
}
QDateEdit QAbstractItemView {
    color: rgb(255, 121, 198);  
    background-color: rgb(33, 37, 43);
/*    padding: 10px;                                           <----  ??? убрать   */
    selection-background-color: rgb(39, 44, 54);
}

/*  Кнопка последнего месяца и кнопка следующего месяца 
    (имя объекта найдено из источника/objectName)    */
#qt_calendar_prevmonth, #qt_calendar_nextmonth {
    border: none; 
    font-weight: bold;

    /* Удалить стандартное изображение клавиши со стрелкой. 
       Вы также можете настроить                        */
    qproperty-icon: none;    
    background-color: rgb(27,29,35)
}
QCalendarWidget QWidget { 
    alternate-background-color: rgb(27,29,35);
}
#qt_calendar_prevmonth {
    qproperty-text: "<"; 
}
#qt_calendar_nextmonth {
    qproperty-text: ">";
}
#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(235, 235, 235, 100);
}

#qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: rgb(113,126,149);
    background-color:rgb(27,29,35);
    min-width: 60px;
    border-radius: 30px;

    margin: -1px -11px -1px -11px;              /* <----<----<----<----<----<---- +++ */
    min-width: 85px;                            /* <----<----<----<----<----<---- +++ */
}

#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(235, 235, 235, 100);
}

/* Поле ввода года        */
#qt_calendar_yearedit {
    color: rgb(113,126,149);
    background: transparent;   

    min-width: 60px;                         /* <----<----<----<----<----<----  +++ */
}
#qt_calendar_yearedit::up-button { 
    color: rgb(27,29,35);
    width: 20px;
    subcontrol-position: right;      
}
#qt_calendar_yearedit::down-button { 
    color: rgb(27,29,35);
    width: 20px;
    subcontrol-position: left;       
}

/* меню выбора месяца           */
CalendarWidget QToolButton QMenu {
     background-color: rgb(33,37,43);
}
CalendarWidget QToolButton QMenu::item {
    padding: 10px;
}
CalendarWidget QToolButton QMenu::item:selected:enabled {
    background-color: rgb(230, 230, 230);
}
CalendarWidget QToolButton::menu-indicator {
    image: none;
}

/* ниже календарной формы */
#qt_calendar_calendarview {
    outline: 0px;           
    selection-background-color: rgb(255,121,198); 
color:rgb(113, 126, 149);
    border-radius: 5px; 
}
'''

app = QApplication(sys.argv)
app.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
app.setStyleSheet(StyleSheet)
window = MainWindow()
window.show()

app.exec()
