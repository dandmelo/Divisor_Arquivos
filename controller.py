# controller.py

from tkinter import filedialog
from view import *
from model import dividir_arquivo_por_linhas

class Controller:
    def __init__(self, root, view):
        self.view = view
        self.root = root      

    def dividir_arquivo(self):
        arquivo_ret = self.view.get_arquivo_original()
        num_partes = int(self.view.get_num_partes())
        pasta_saida = self.view.get_pasta_saida()
        num_linhas_cabecalho = int(self.view.get_num_linhas_cabecalho())
        num_linhas_rodape = int(self.view.get_num_linhas_rodape())

        
        # Chame a função do modelo para dividir o arquivo
        dividir_arquivo_por_linhas(arquivo_ret, num_partes, pasta_saida, num_linhas_cabecalho, num_linhas_rodape)    

        # Atualize o status na visão
        self.view.mostrar_status("")

    def selecionar_arquivo_original(self):
        arquivo_ret = filedialog.askopenfilename(filetypes=[("Arquivos RET", "*.ret"), ('Arquivos TXT', '*.txt')])
        if arquivo_ret:
            self.view.entrada_arquivo_original.delete(0, tk.END)
            self.view.entrada_arquivo_original.insert(0, arquivo_ret)

    def selecionar_diretorio_saida(self):
        pasta_saida = filedialog.askdirectory(title="Selecione o Diretório de Saída")
        if pasta_saida:
            self.view.entrada_diretorio_saida.delete(0, tk.END)
            self.view.entrada_diretorio_saida.insert(0, pasta_saida)
    
    def configurar_eventos(self):  # cria um método para configurar os eventos da view
        self.view.botao_dividir.config(command=self.dividir_arquivo)

        self.view.botao_selecionar_arquivo_original.config(command=self.selecionar_arquivo_original)
        self.view.botao_selecionar_diretorio_saida.config(command=self.selecionar_diretorio_saida)

    

