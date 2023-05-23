import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton #подключение библиотек

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self) 
        self.hbox_first = QHBoxLayout() #создание слоёв
        self.hbox_input = QHBoxLayout() #создание слоёв

        self.hbox_result = QHBoxLayout() #создание слоёв

        self.hbox_second = QHBoxLayout() #создание слоёв
        self.hbox_third = QHBoxLayout() #создание слоёв
        self.hbox_fourth = QHBoxLayout() #создание слоёв



        self.vbox.addLayout(self.hbox_input) #создание слоёв
        self.vbox.addLayout(self.hbox_first) #создание слоёв

        self.vbox.addLayout(self.hbox_second) #создание слоёв
        self.vbox.addLayout(self.hbox_third) #создание слоёв
        self.vbox.addLayout(self.hbox_fourth) #создание слоёв
        self.vbox.addLayout(self.hbox_result) #создание слоёв




        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        # Кнопки

        self.b_result = QPushButton("=", self) #создание кнопки
        self.hbox_result.addWidget(self.b_result)

        # First layer
        self.b_1 = QPushButton("1", self) #создание кнопки
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self) #создание кнопки
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self) #создание кнопки
        self.hbox_first.addWidget(self.b_3)

        self.b_div = QPushButton("/", self) #создание кнопки
        self.hbox_first.addWidget(self.b_div)

        # Second layer
        self.b_4 = QPushButton("4", self) #создание кнопки
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self) #создание кнопки
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self) #создание кнопки
        self.hbox_second.addWidget(self.b_6)

        self.b_minus = QPushButton("-", self) #создание кнопки
        self.hbox_second.addWidget(self.b_minus)

        # Third layer
        self.b_7 = QPushButton("7", self) #создание кнопки
        self.hbox_third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self) #создание кнопки
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self) #создание кнопки
        self.hbox_third.addWidget(self.b_9)

        self.b_plus = QPushButton("+", self) #создание кнопки
        self.hbox_third.addWidget(self.b_plus)

        # Fourth layer
        self.b_point = QPushButton(".", self) #создание кнопки
        self.hbox_fourth.addWidget(self.b_point)

        self.b_0 = QPushButton("0", self) #создание кнопки
        self.hbox_fourth.addWidget(self.b_0)

        self.b_erase = QPushButton("<-", self) #создание кнопки
        self.hbox_fourth.addWidget(self.b_erase)

        self.b_multiply = QPushButton("*", self) #создание кнопки
        self.hbox_fourth.addWidget(self.b_multiply)


        self.op = '+' #сложение по умолчанию 
        self.num_1 = 0 #ноль по умолчанию 
        self.num_2 = 0 #ноль по умолчанию 

        # События
        self.b_plus.clicked.connect(lambda: self._operation("+")) #привязка события к кнопке
        self.b_result.clicked.connect(self._result) #привязка события к полю вывода результата


        self.b_1.clicked.connect(lambda: self._button("1")) #привязка события к кнопке
        self.b_2.clicked.connect(lambda: self._button("2")) #привязка события к кнопке
        self.b_3.clicked.connect(lambda: self._button("3")) #привязка события к кнопке

        self.b_4.clicked.connect(lambda: self._button("4")) #привязка события к кнопке
        self.b_5.clicked.connect(lambda: self._button("5")) #привязка события к кнопке
        self.b_6.clicked.connect(lambda: self._button("6")) #привязка события к кнопке
        self.b_7.clicked.connect(lambda: self._button("7")) #привязка события к кнопке
        self.b_8.clicked.connect(lambda: self._button("8")) #привязка события к кнопке
        self.b_9.clicked.connect(lambda: self._button("9")) #привязка события к кнопке
        self.b_0.clicked.connect(lambda: self._button("0")) #привязка события к кнопке

        self.b_minus.clicked.connect(lambda: self._operation("-")) #привязка события к кнопке
        self.b_multiply.clicked.connect(lambda: self._operation("*")) #привязка события к кнопке
        self.b_div.clicked.connect(lambda: self._operation("/")) #привязка события к кнопке

        self.b_point.clicked.connect(lambda: self._button(".")) #привязка события к кнопке
        self.b_erase.clicked.connect(self._erase_text) #привязка события к кнопке

    # Обработка ввода
    def _button(self, param):
        line = self.input.text() #запись новой цифры
        self.input.setText(line + param) #добавление новой цифры в поле ввода

    # Обработка операций
    def _operation(self, op):
        if self.input.text() == '': #если текст не введён, то 0
            self.num_1 = 0
        else: self.num_1 = float(self.input.text()) #преобразуется в float

        self.op = op #запись действия (арифметического)
        self.input.setText("") #если действия отсутствует, то ставит пустоту

    # Обработка результа
    def _result(self):
        if self.input.text() == '': #проверка на действие
            self.num_2 = 0
        else: self.num_2 = float(self.input.text()) #проверка на действие

        if self.op == "+": #проверка на действие
            self.input.setText(str(self.num_1 + self.num_2))

        elif self.op == "-": #проверка на действие
            self.input.setText(str(self.num_1 - self.num_2))

        elif self.op == "/": #проверка на действие
            self.input.setText(str(self.num_1 / self.num_2))

        elif self.op == "*": #проверка на действие
            self.input.setText(str(self.num_1 * self.num_2))

    def _erase_text(self): #функция кнопки "Сброс"
        self.input.setText('')

app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())
