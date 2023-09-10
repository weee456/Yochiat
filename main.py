from PyQt5.QtCore import *
from PyQt5.QtWebEngineCore import *
from PyQt5.QtWidgets import *

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.show()
