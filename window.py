import sys
import os
import pandas as pd
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from concatenadorQT import Ui_MainWindow

class ConcatenadorPlanilhas(QMainWindow):
    def __init__(self):
        super(ConcatenadorPlanilhas, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Concatenador de Planilhas")
        self.setWindowIcon(QIcon('C:\\Users\\Luis Tvc\\Documents\\Concatenador de planinhas\\KMD.png'))  

        fixed_width = 418
        fixed_height = 321
        self.setFixedSize(fixed_width, fixed_height)

        # Conectando os botões com as funções
        self.ui.selecionarExcel.clicked.connect(self.selecionar_diretorio)
        self.ui.executar.clicked.connect(self.concatenar_planilhas)
        # Desativa o botão 'Executar' inicialmente
        self.ui.executar.setEnabled(False)  

        # Inicializa a barra de progresso em zero
        self.ui.barraProgresso.setValue(0)  
        
        # Personalização dos botões 
        self.ui.executar.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                font-size: 14px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FF0000;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)

        self.ui.selecionarExcel.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                font-size: 13px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FF0000;
            }
        """)

        # Personalização da barra de progresso
        self.ui.barraProgresso.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                width: 20px;
            }
        """)

        # Variável para guardar o diretório selecionado
        self.diretorio = ""

    def selecionar_diretorio(self):
        # Abrir a janela para selecionar o diretório
        self.diretorio = QFileDialog.getExistingDirectory(self, "Selecionar Diretório", "")
        
        # Se um diretório for selecionado, habilitar o botão 'Executar'
        if self.diretorio:
            self.ui.executar.setEnabled(True)
            if hasattr(self.ui, 'log'):
                 # Verifica se o log existe antes de usar
                self.ui.log.append(f"Diretório selecionado: {self.diretorio}")
        else:
            if hasattr(self.ui, 'log'):
                self.ui.log.append("Nenhum diretório selecionado.")
    
    def concatenar_planilhas(self):
        try:
            # Buscar todos os arquivos Excel no diretório selecionado
            arquivos_excel = [f for f in os.listdir(self.diretorio) if f.endswith('.xlsx')]
            total_arquivos = len(arquivos_excel)
            
            if total_arquivos == 0:
                if hasattr(self.ui, 'log'):
                    self.ui.log.append("Nenhum arquivo Excel encontrado no diretório.")
                return
            
            if hasattr(self.ui, 'log'):
                self.ui.log.append(f"{total_arquivos} arquivos encontrados.")
            
            # Inicializa uma lista para armazenar os DataFrames de cada arquivo
            dataframes = []
            
            # Reseta a barra de progresso para 0
            self.ui.barraProgresso.setValue(0)
            
            for i, arquivo in enumerate(arquivos_excel):
                caminho_arquivo = os.path.join(self.diretorio, arquivo)
                
                try:
                    # Tenta ler o arquivo Excel
                    df = pd.read_excel(caminho_arquivo)
                    
                    # Verifica se as colunas estão corretamente alinhadas com o cabeçalho
                    if df.shape[1] == df.columns.size:
                        df = df.dropna(how='all', axis=0)
                        df = df[df.apply(lambda row: row.notna().sum() > 1, axis=1)]
                        
                        dataframes.append(df)
                        if hasattr(self.ui, 'log'):
                            self.ui.log.append(f"Arquivo {arquivo} lido com sucesso.")
                    else:
                        if hasattr(self.ui, 'log'):
                            self.ui.log.append(f"Arquivo {arquivo} ignorado por não estar no formato correto.")
                    
                    progresso = int(((i + 1) / total_arquivos) * 100)
                    self.ui.barraProgresso.setValue(progresso)
                
                except Exception as e:
                    if hasattr(self.ui, 'log'):
                        self.ui.log.append(f"Erro ao ler o arquivo {arquivo}: {str(e)}")
                    continue
            
            if dataframes:
                df_concatenado = pd.concat(dataframes, ignore_index=True)
                arquivo_saida = os.path.join(self.diretorio, "planilhas_concatenadas.xlsx")
                df_concatenado.to_excel(arquivo_saida, index=False)
                if hasattr(self.ui, 'log'):
                    self.ui.log.append(f"Arquivos concatenados com sucesso. Arquivo salvo em: {arquivo_saida}")
            else:
                if hasattr(self.ui, 'log'):
                    self.ui.log.append("Nenhum arquivo foi encontrado para concatenar.")
            
            self.ui.barraProgresso.setValue(100)

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro durante o processo: {str(e)}")
            if hasattr(self.ui, 'log'):
                self.ui.log.append(f"Erro geral: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ConcatenadorPlanilhas()
    janela.show()
    sys.exit(app.exec())
