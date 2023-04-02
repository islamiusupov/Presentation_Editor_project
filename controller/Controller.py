from model.Model import Model


class Controller:
    def __init__(self, mw, ew, sw):
        self.mainwin = mw
        self.editwin = ew
        self.slidewin = sw
        self.model = Model(self.mainwin, self.editwin, self.slidewin)
        self.connect_mainwindow()
        self.connect_editor_window()
        self.connect_slide_show_window()

    def connect_mainwindow(self):
        self.mainwin.editor_btn.clicked.connect(self.model.open_editor)
        self.mainwin.add_slide_btn.clicked.connect(self.model.addtab)
        self.mainwin.remove_slide_btn.clicked.connect(self.model.removetab)
        self.mainwin.slide_show_btn.clicked.connect(self.model.open_slideshow)

    def connect_editor_window(self):
        self.editwin.add_image_btn.clicked.connect(self.model.addImage)
        self.editwin.add_text_btn.clicked.connect(self.model.addText)

    def connect_slide_show_window(self):
        self.slidewin.back_btn.clicked.connect(self.model.back)
        self.slidewin.next_btn.clicked.connect(self.model.next)
        self.slidewin.stop_btn.clicked.connect(self.model.stop)
        self.slidewin.closeEvent = lambda event: self.model.closeEvent(event)


