import sys

from PyQt5.QtWidgets import QApplication

from controller.Controller import Controller
from view.main_view import MainWindow, EditorWindow, SlideShowWindow
from model.Model import Model

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_view = MainWindow()
    editwin = EditorWindow()
    slidewin = SlideShowWindow()
    editwin.setFixedSize(784, 165)
    slidewin.setFixedSize(791, 638)
    controller = Controller(main_view, editwin, slidewin)
    model = Model(main_view, editwin, slidewin)
    main_view.show()
    sys.exit(app.exec_())
