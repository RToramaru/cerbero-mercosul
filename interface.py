from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def click_start(self):
        self.input_text.hide()
        self.button_start.hide()
        self.button_stop.show()
        
    def click_stop(self):
        self.input_text.show()
        self.button_start.show()
        self.button_stop.hide()

    def __init__(self):
        super().__init__()
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Cérbero")
        self.window.setGeometry(100,100,400,400)
        self.window.setFixedSize(400,400)
        self.window.setObjectName("window")
        self.desktopRect = QtWidgets.QApplication.desktop().availableGeometry()
        self.window.move(self.desktopRect.center() - self.window.rect().center())
        self.window.setStyleSheet("#window{background-image: url(images/background.jpg);}")
        self.window.setWindowIcon(QtGui.QIcon("images/background.jpg"))
        self.label_panel = QtWidgets.QLabel(self.window)
        self.label_panel.setFixedSize(300,300)
        self.label_panel.move(50, 50)
        self.label_panel.setStyleSheet("background-color: rgba(255,255,255,0.9);")
        self.input_text = QtWidgets.QLineEdit(self.window)
        self.input_text.setPlaceholderText("Endereço IP da camera")
        self.style_text = """
            background-color: rgb(255, 255, 255);
            font-size: 14px; 
            font-weight: bold; 
            color: rgb(0, 0, 0); 
            border-radius: 24px; 
            padding-left: 20px; 
            padding-right: 20px; 
            border-color: rgb(127, 127, 127); 
            border-width: 2px; 
            border-style: solid;
        """
        self.input_text.setStyleSheet(self.style_text)
        self.input_text.setGeometry(100, 135, 220, 55)
        self.button_start = QtWidgets.QPushButton("Conectar", self.window)
        self.style_button_start = """
            background-color: rgb(34, 177, 76);
            font-size: 16px; 
            font-weight: bold; 
            color: rgb(0, 0, 0); 
            border-radius: 24px;
            color: rgb(255, 255, 255);
        """
        self.button_start.setStyleSheet(self.style_button_start)
        self.button_start.setGeometry(100, 205, 220, 55)
        self.button_stop = QtWidgets.QPushButton("Desconactar", self.window)
        self.style_button_stop = """
            background-color: rgb(237, 28, 36);self.
            font-size: 16px; 
            font-weight: bold; 
            color: rgb(0, 0, 0); 
            border-radius: 24px;
            color: rgb(255, 255, 255);
        """
        self.button_stop.setStyleSheet(self.style_button_stop)
        self.button_stop.setGeometry(100, 250, 220, 55)
        self.button_stop.hide()
        self.button_start.clicked.connect(self.click_start)
        self.button_stop.clicked.connect(self.click_stop)
        self.window.show()
        sys.exit(app.exec_())
if(__name__ == "__main__"):
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow()