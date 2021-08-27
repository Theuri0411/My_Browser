import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://github.com/Theuri0411"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # NAVIGATION BAR
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_button = QAction("BACKWARD", self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        forward_button = QAction("FORWARD", self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        reload_button = QAction("REFRESH", self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        home_button = QAction("HOME", self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        def navigate_home(self):
            self.browser.setUrl(QUrl("https://google.com"))


app = QApplication(sys.argv)
QApplication.setApplicationDisplayName("MY_BROWSER")
window = MainWindow()
app.exec_()
