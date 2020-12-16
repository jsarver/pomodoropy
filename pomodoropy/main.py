import sys
import time

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLabel, QTextEdit, QPlainTextEdit, QMessageBox
from PySide2.QtCore import QFile, QObject, QTimer, Qt
from PySide2 import QtWidgets
from win10toast import ToastNotifier


toaster = ToastNotifier()


class Config(object):
    def __init__(self, notify_type, duration=1500):
        self.notifyType = notify_type
        self.duration = duration


cfg = Config("modal")

class Form(QObject):

    def __init__(self, ui_file, parent=None, client=None, config=cfg):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        self.start = False
        self.duration = cfg.duration
        self.count = cfg.duration
        self.current_task = ""
        self.window.setWindowModality(Qt.ApplicationModal)
        self.window.setFocusPolicy(Qt.StrongFocus)

        # creating start button
        start_button = self.window.findChild(QPushButton, 'startButton')
        start_button.clicked.connect(self.start_action)

        toggle_button = self.window.findChild(QPushButton, 'toggleButton')
        toggle_button.clicked.connect(self.toggle_action)

        # creating pause button
        pause_button = self.window.findChild(QPushButton, 'pauseButton')
        pause_button.clicked.connect(self.pause_action)

        reset_button = self.window.findChild(QPushButton, 'resetButton')
        reset_button.clicked.connect(self.reset_action)

        add_button = self.window.findChild(QPushButton, 'addButton')
        add_button.clicked.connect(self.add_task)

        self.timerText = self.window.findChild(QPushButton, 'toggleButton')

        # creating a timer object
        self.timer = QTimer(self)

        # adding action to timer
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        # setting label text
        self.timerText.setText(f"{int(self.duration / 60)}")
        # self.window.destroyed.connect(self.window.close)

        self.window.show()

    def toggle_action(self):
        print(f"staring action {self.start}")
        if self.start:
            print("pause")
            self.pause_action()

        elif not self.start:
            print("start")
            self.start_action()

    def start_action(self):
        # making flag true
        self.start = True
        if self.count == 0:
            self.reset_action()
        print(f'starting {self.count}')
        self.notify("starting Timer", self.current_task, notify_type="toast",toast_duration=2)


    def pause_action(self):
        # making flag false
        self.start = False

    def reset_action(self):
        # making flag false
        self.start = False
        self.count = self.duration
        self.timerText.setText(f"{self.count / 60:.0f}")

    def updateTime(self):
        if self.start:
            if self.count > 0:
                self.count -= 1
                text = str(f"{int(self.count / 60)}.{self.count % 60}")
                self.timerText.setText(text)
            else:
                self.start = False
                self.count = 0
                text = str(self.count)
                self.timerText.setText(text)
                self.notify("Timer Done",self.current_task,"toast")

    def notify(self,title, message,notify_type="modal",toast_duration=5):
        notify_type = notify_type if notify_type else cfg.notifyType
        if notify_type == "modal":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(message)
            msg.setWindowTitle(title)
            msg.exec_()

        else:
            self.window.raise_()
            self.window.activateWindow()
            toaster.show_toast(title,
                               message,
                               icon_path=None,
                               duration=toast_duration,
                               threaded=True)
    def add_task(self):
        task = self.window.findChild(QPlainTextEdit, "addTaskTextEdit")
        taskLabel = self.window.findChild(QLabel, "currentTaskLabel")
        self.current_task = task.toPlainText()
        taskLabel.setText(task.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("cleanlooks")
    form = Form('timer.ui')

    print('start exit')
    sys.exit(app.exec_())
