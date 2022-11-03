from PySide2 import QtGui, QtWidgets
from PySide2extn.RoundProgressBar import roundProgressBar
import sys
from detection_cerbero import detection
import threading

class Ui_MainWindow(object):     
    # funcao para chmar a deteccao de placa    
    def detection_plate(self):
        detection.execute.execute(self.input_text.text())
    # funcao quando o botao de conectar for clicado
    def click_start(self):
        # oculta os campos e exibe a mensagem de deteccao
        self.input_text.hide()
        self.button_start.hide()
        self.label_detection.show()
        # cria uma thread para executar a deteccao
        th = threading.Thread(target=self.detection_plate)
        th.start()
    # funcao para iniciar a interface
    def __init__(self, app):
        super().__init__()
        # cria a janela com o titulo e a dimensao
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Cérbero")
        self.window.setGeometry(100, 100, 400, 400)
        self.window.setFixedSize(400, 400)
        self.window.setObjectName("window")
        desktopRect = QtWidgets.QApplication.primaryScreen().availableGeometry()
        # centraliza a janela
        self.window.move(desktopRect.center() - self.window.rect().center())
        # adiciona a imagem de fundo
        self.window.setStyleSheet("#window{background-image: url(images/background.jpg);}")
        self.window.setWindowIcon(QtGui.QIcon("../images/background.jpg"))
        # cria um painel branco no centro da janela
        self.label_panel = QtWidgets.QLabel(self.window)
        self.label_panel.setFixedSize(300, 300)
        self.label_panel.move(50, 50)
        self.label_panel.setStyleSheet("background-color: rgba(255,255,255,0.8);border-radius: 24px;")
        # cria um input para o usuario digitar a url do video
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
        # cria um texto para exibir a mensagem de deteccao e deixa invisivel
        self.label_detection = QtWidgets.QLabel(self.window)
        self.label_detection.setFixedSize(300, 300)
        self.label_detection.move(150, 0)
        self.label_detection.setText("Detectando...")
        self.label_detection.setStyleSheet("font-size: 20px;color: rgb(0, 159, 227);")
        self.label_detection.hide()
        # cria um botao para iniciar a deteccao
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
        # executa a funcao click_start quando o botao for clicado
        self.button_start.clicked.connect(self.click_start)
        # exibe a janela
        self.window.show()
        sys.exit(app.exec_())

class execute():
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow(app)

if (__name__ == "__main__"):
    execute()
