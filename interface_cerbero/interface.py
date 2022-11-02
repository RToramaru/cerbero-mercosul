from PySide2 import QtCore, QtGui, QtWidgets
from PySide2extn.RoundProgressBar import roundProgressBar
import sys
from detection_cerbero import detection
import threading

class Ui_MainWindow(object):     
        
    def detection_plate(self):
        detection.execute.execute(self.input_text.text())

    def click_start(self):
        self.input_text.hide()
        self.button_start.hide()
        self.label_detection.show()
        th = threading.Thread(target=self.detection_plate)
        th.start()

    def setProgress(self):
        self.label_detection.show()

    def retranslateUi(self):
        self.worker.start()

    def __init__(self, app):
        super().__init__()
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Cérbero")
        self.window.setGeometry(100, 100, 400, 400)
        self.window.setFixedSize(400, 400)
        self.window.setObjectName("window")
        desktopRect = QtWidgets.QApplication.primaryScreen().availableGeometry()
        self.window.move(desktopRect.center() - self.window.rect().center())
        self.window.setStyleSheet("#window{background-image: url(../images/background.jpg);}")
        self.window.setWindowIcon(QtGui.QIcon("../images/background.jpg"))
        self.label_panel = QtWidgets.QLabel(self.window)
        self.label_panel.setFixedSize(300, 300)
        self.label_panel.move(50, 50)
        self.label_panel.setStyleSheet("background-color: rgba(255,255,255,0.8);border-radius: 24px;")
        self.input_text = QtWidgets.QLineEdit(self.window)
        self.input_text.setPlaceholderText("Endereço IP da camera")
        style_text = """
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
        self.input_text.setStyleSheet(style_text)
        self.input_text.setGeometry(100, 135, 220, 55)
        self.round_progressbar = roundProgressBar(self.window)
        self.round_progressbar.setGeometry(200, 200, 220, 55)
        self.round_progressbar.move(170, 170)
        self.round_progressbar.hide()
        self.label_detection = QtWidgets.QLabel(self.window)
        self.label_detection.setFixedSize(300, 300)
        self.label_detection.move(150, 0)
        self.label_detection.setText("Detectando...")
        self.label_detection.setStyleSheet("font-size: 20px;color: rgb(0, 159, 227);")
        self.label_detection.hide()
        self.button_start = QtWidgets.QPushButton("Conectar", self.window)
        style_button_start = """
            background-color: rgb(34, 177, 76);
            font-size: 16px; 
            font-weight: bold; 
            color: rgb(0, 0, 0); 
            border-radius: 24px;
            color: rgb(255, 255, 255);
        """
        self.button_start.setStyleSheet(style_button_start)
        self.button_start.setGeometry(100, 205, 220, 55)
        self.button_start.clicked.connect(self.click_start)
        self.window.show()
        sys.exit(app.exec_())

class execute():
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow(app)

if (__name__ == "__main__"):
    execute()
