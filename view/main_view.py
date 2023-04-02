from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/firstform.ui', self)
        self.setWindowTitle('Редактор презентаций')
        self.setFixedSize(792, 608)


class EditorWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/secondform.ui', self)
        self.setWindowTitle('Редактор')


class SlideShowWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")
        uic.loadUi('view/slideshow.ui', self)
        self.setWindowTitle('Слайд-шоу')




