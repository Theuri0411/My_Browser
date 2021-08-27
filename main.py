import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # NAVIGATION BAR
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_button = QAction("Back", self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        forward_button = QAction("forward", self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        reload_button = QAction("Reload", self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)



app = QApplication(sys.argv)
QApplication.setApplicationDisplayName("My_Browser")
window = MainWindow()
app.exec_()
