import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal

class LogWatcher(QThread):
    log_signal = pyqtSignal(str)

    def run(self):
        # Dummy log watching logic; replace with actual log reading
        while True:
            log_message = "Log message..."
            self.log_signal.emit(log_message)
            self.msleep(1000)  # Wait for a second before emitting next log

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple QTool')
        self.setGeometry(100, 100, 600, 400)

        self.log_watcher = LogWatcher()
        self.log_watcher.log_signal.connect(self.update_log)
        self.log_watcher.start()

    def update_log(self, message):
        print(message)  # Replace with actual log handling logic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
