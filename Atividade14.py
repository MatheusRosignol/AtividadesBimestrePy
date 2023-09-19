import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit

class MainJanela(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.conjunto_widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.conjunto_widget.setLayout(self.v_layout)

        self.label1 = QLabel("Esse quadradinho aqui??...")
        self.v_layout.addWidget(self.label1)
        self.setCentralWidget(self.conjunto_widget)

    def atualizar_label(self, nome, mensagem):
       
        texto = f"Nome: {nome}\nMensagem: {mensagem}"
        self.label1.setText(texto)

class NovaJanela(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PALMEIRAS NÃO TEM MUNDIAL")
        self.setGeometry(100, 100, 300, 200)

       
        self.nome_label = QLabel("Coloca o Nome aqui:")
        self.nome_input = QLineEdit()
        self.mensagem_label = QLabel("Com relação ao desempenho do Pameiras, qual seu veredito?")
        self.mensagem_input = QTextEdit()
        self.zoeira_label = QLabel("É zoeira tá professor haha escreve ai que sou um bom aluno!")
        self.zoeira_input = QTextEdit()

        
        self.botao_enviar = QPushButton("Fazer o que né, ENVIAR DE UMA VEZ")
        self.botao_enviar.clicked.connect(self.enviar_mensagem)

        
        layout = QVBoxLayout()
        layout.addWidget(self.nome_label)
        layout.addWidget(self.nome_input)
        layout.addWidget(self.mensagem_label)
        layout.addWidget(self.mensagem_input)
        layout.addWidget(self.zoeira_label)
        layout.addWidget(self.zoeira_input)
        layout.addWidget(self.botao_enviar)
        self.setLayout(layout)

    def enviar_mensagem(self):
       
        nome = self.nome_input.text()
        mensagem = self.mensagem_input.toPlainText()

        
        self.main_window.atualizar_label(nome, mensagem)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainJanela()
    main_window.setWindowTitle("Título aqui!!")
    main_window.show()

    nova_janela = NovaJanela(main_window)
    nova_janela.setStyleSheet("background-color: green;")
    nova_janela.show()

    sys.exit(app.exec())