from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (QAction, QDesktopWidget, QHBoxLayout, QHeaderView,
                             QLabel, QMainWindow, QMenu, QTableView,
                             QVBoxLayout, QWidget, qApp)

from server.add_user import RegisterUser
from server.configuration_window import ConfigurationWindow
from server.history_window import HistoryWindow
from server.remove_user import RemoveUser


class MainWindow(QMainWindow):
    """
    Класс - основное окно серверной части.
    Основным виджетом окна является таблица пользователей онлайн,
    которая автоматически обновляется каждую секунду.
    """

    def __init__(self, database, server, settings):
        super().__init__()
        self.database = database
        self.server_thread = server
        self.settings = settings

        exit_action = QAction('Выход', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)

        self.menuBar = self.menuBar()

        self.history_view_button = QAction('История клиентов', self)
        self.configuration_button = QAction('Настройки сервера', self)
        self.refresh_button = QAction('Обновить список клиентов', self)
        self.register_button = QAction('Зарегистрировать пользователя', self)
        self.remove_button = QAction('Удалить пользователя', self)

        self.users_menu = QMenu('Пользователи', self)
        self.users_menu.addAction(self.refresh_button)
        self.users_menu.addAction(self.register_button)
        self.users_menu.addAction(self.remove_button)

        self.menuBar.addAction(exit_action)
        self.menuBar.addMenu(self.users_menu)
        self.menuBar.addAction(self.configuration_button)
        self.menuBar.addAction(self.history_view_button)

        self.configuration_button.triggered.connect(self.show_configuration)
        self.history_view_button.triggered.connect(self.show_history)

        self.refresh_button.triggered.connect(self.active_users_table_create)
        self.register_button.triggered.connect(self.show_registration)
        self.remove_button.triggered.connect(self.show_removing)

        self.setMinimumHeight(300)
        self.setMinimumWidth(500)
        self.resize(self.minimumWidth(), self.minimumHeight())
        self.setWindowTitle('Buinichenko Mikhail server GUI')

        self.label = QLabel('Список подключенных клиентов:', self)
        self.label.adjustSize()

        self.active_users_table = QTableView(self)

        window = QWidget()

        verticalLayout = QVBoxLayout()
        horizontalLayout = QHBoxLayout()

        horizontalLayout.addWidget(self.active_users_table)
        verticalLayout.addWidget(self.label)
        verticalLayout.addLayout(horizontalLayout)

        window.setLayout(verticalLayout)

        self.setCentralWidget(window)

        self.timer = QTimer()
        self.timer.timeout.connect(self.active_users_table_create)
        self.timer.start(1000)

        self.show()

    def center(self):
        """
        Метод, осуществляющий центрирование основного окна.

        :return: ничего не возвращает.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def active_users_table_create(self):
        """
        Метод, заполняющий таблицу пользователей онлайн.

        :return: ничего не возвращает.
        """
        users_list = self.database.active_users_list()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Имя пользователя', 'IP-адрес', 'Порт подключения', 'Время подключения', ])
        for row in users_list:
            username, address, port, time = row

            username = QStandardItem(username)
            username.setEditable(False)

            address = QStandardItem(address)
            address.setEditable(False)

            port = QStandardItem(str(port))
            port.setEditable(False)

            time = QStandardItem(str(time.replace(microsecond=0)))
            time.setEditable(False)

            model.appendRow([username, address, port, time])

        self.active_users_table.setModel(model)
        self.active_users_table_headers = self.active_users_table.horizontalHeader()
        self.active_users_table_headers.setSectionResizeMode(0, QHeaderView.Stretch)
        self.active_users_table_headers.setSectionResizeMode(1, QHeaderView.Stretch)
        self.active_users_table_headers.setSectionResizeMode(2, QHeaderView.Stretch)
        self.active_users_table_headers.setSectionResizeMode(3, QHeaderView.Stretch)

    def show_history(self):
        """
        Метод, вызывающий окно со статистикой клиентов.

        :return: ничего не возвращает.
        """
        global history_window
        history_window = HistoryWindow(self.database)
        history_window.show()

    def show_configuration(self):
        """
        Метод, вызывающий окно с настройками сервера.

        :return: ничего не возвращает.
        """
        global settings_window
        settings_window = ConfigurationWindow(self.settings)
        settings_window.show()

    def show_registration(self):
        """
        Метод, вызывающий окно регистрации пользователя.

        :return: ничего не возвращает.
        """
        global registration_window
        registration_window = RegisterUser(self.database, self.server_thread)
        registration_window.show()

    def show_removing(self):
        """
        Метод, вызывающий окно удаления пользователя.

        :return: ничего не возвращает.
        """
        global remove_window
        remove_window = RemoveUser(self.database, self.server_thread)
        remove_window.show()
