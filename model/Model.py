from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.QtWidgets import QWidget, QFileDialog, QInputDialog, QLabel


class Model:
    def __init__(self, main, edit, slide):
        self.main_window = main
        self.editor_window = edit
        self.slide_show_window = slide


    def open_editor(self):
        self.editor_window.show()

    def open_slideshow(self):
        self.main_window.tabWidget.hide()
        self.main_window.tabWidget.setParent(self.slide_show_window)
        self.main_window.tabWidget.show()
        self.slide_show_window.show()

    def addtab(self):
        self.main_window.tabWidget.addTab(QWidget(), f" Слайд {self.main_window.tabWidget.count() + 1}")

    def removetab(self):
        self.main_window.tabWidget.removeTab(self.main_window.tabWidget.currentIndex())
        for i in range(self.main_window.tabWidget.count()):
            self.main_window.tabWidget.setTabText(i, f'Слайд {i + 1}')

    def next(self):
        if self.main_window.tabWidget.currentIndex() != (self.main_window.tabWidget.count() - 1):
            self.main_window.tabWidget.setCurrentIndex(self.main_window.tabWidget.currentIndex() + 1)
        else:
            self.main_window.tabWidget.setCurrentIndex(0)

    def back(self):
        if self.main_window.tabWidget.currentIndex() != 0:
            self.main_window.tabWidget.setCurrentIndex(self.main_window.tabWidget.currentIndex() - 1)
        else:
            self.main_window.tabWidget.setCurrentIndex(self.main_window.tabWidget.count() - 1)

    def stop(self):
        self.main_window.tabWidget.hide()
        self.main_window.tabWidget.setParent(self.main_window)
        self.main_window.tabWidget.show()
        self.slide_show_window.close()

    def closeEvent(self, a0):
        self.main_window.tabWidget.hide()
        self.main_window.tabWidget.setParent(self.main_window)
        self.main_window.tabWidget.show()
        a0.accept()

    def getImageGeometry(self):
        try:
            x = int(self.editor_window.height_2.text())
            y = int(self.editor_window.width_2.text())
            w = int(self.editor_window.height.text())
            h = int(self.editor_window.width.text())
        except:
            x = 0
            y = 0
            w = 100
            h = 100

        return QRect(x, y, w, h)


    def addImage(self):
        result = QFileDialog.getOpenFileName(self.editor_window, 'Выбрать картинку', '')
        if result[1]:
            try:
                image = QImage(result[0])
                label = QLabel('', self.main_window.tabWidget.currentWidget())
                label.setPixmap(QPixmap.fromImage(image).scaled(int(self.editor_window.height.text()),
                                                                int(self.editor_window.width.text()),
                                                                Qt.KeepAspectRatio))
                label.move(int(self.editor_window.height_2.text()), int(self.editor_window.width_2.text()))
                label.show()
            except:
                image = QImage(result[0])
                label = QLabel('', self.main_window.tabWidget.currentWidget())
                label.setPixmap(QPixmap.fromImage(image))
                label.move(0, 0)
                label.adjustSize()
                label.show()

    def addText(self):
        result = QInputDialog.getText(self.editor_window, 'Введите текст', 'введите текст')
        if result[1]:
            try:
                label = QLabel(result[0], self.main_window.tabWidget.currentWidget())
                label.move(int(self.editor_window.height_2.text()), int(self.editor_window.width_2.text()))
                label.setFont(QFont(self.editor_window.lineEdit_2.text(), int(self.editor_window.lineEdit.text())))
                label.adjustSize()
                label.show()

            except:
                label = QLabel(result[0], self.main_window.tabWidget.currentWidget())
                label.move(0, 0)
                label.setFont(QFont('Times', 10))
                label.adjustSize()
                label.show()
