# view.py

import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter.messagebox import showinfo
import controller
import base64
from PIL import Image, ImageTk
import io
import time

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Dividir Arquivos .ret, .txt")
        self.root.geometry("600x200")
        # self.root.grid()        

        self.controller = controller.Controller(self.root, self)
       
        # Instruções
        label_instrucoes = tk.Label(root, text="Divisor de Arquivos", font=('verdana', '12', 'bold'))
        label_instrucoes.pack()

        # Número Partes
        frame_num_partes = tk.Frame(root)
        frame_num_partes.place(x=10, y=40)
        # frame_num_partes.grid(row=1, column=1)

        label_num_partes = tk.Label(frame_num_partes, text="Número de Partes:")
        label_num_partes.pack(side=tk.LEFT)
        # label_num_partes.grid(row=1, column=2)

        # ComboBox para selecionar o número de partes
        self.combo_num_partes = ttk.Combobox(frame_num_partes, values=list(range(2, 11)), width=16)
        self.combo_num_partes.set(2)  # Defina o valor padrão como 2
        self.combo_num_partes.pack(side=tk.LEFT, padx=20)

        # Arquivo Original
        frame_arquivo_original = tk.Frame(root)
        frame_arquivo_original.place(x=10, y=70)

        label_arquivo_original = tk.Label(frame_arquivo_original, text="Arquivo Original:")
        label_arquivo_original.pack(side=tk.LEFT)

        self.entrada_arquivo_original = tk.Entry(frame_arquivo_original, width=45)
        self.entrada_arquivo_original.pack(side=tk.LEFT, padx=28)

        self.botao_selecionar_arquivo_original = tk.Button(frame_arquivo_original, width=20, text="Selecionar Arquivo", command=self.selecionar_arquivo_original)
        self.botao_selecionar_arquivo_original.pack(side=tk.LEFT, padx=4)

        # Diretório Saída
        frame_diretorio_saida = tk.Frame(root)
        frame_diretorio_saida.place(x=10, y=100)

        label_diretorio_saida = tk.Label(frame_diretorio_saida, text="Diretório de Saída:")
        label_diretorio_saida.pack(side=tk.LEFT)

        # self.entrada_diretorio_saida = tk.Entry(frame_diretorio_saida, width=40)
        self.entrada_diretorio_saida = tk.Entry(frame_diretorio_saida, width=45)
        self.entrada_diretorio_saida.pack(side=tk.LEFT, padx=22)

        self.botao_selecionar_diretorio_saida = tk.Button(frame_diretorio_saida, width=20, text="Selecionar Diretório", command=self.selecionar_diretorio_saida)
        self.botao_selecionar_diretorio_saida.pack(side=tk.LEFT, padx=10)

        # Configurações Cabeçalho e Rodapé
        frame_configuracoes = tk.Frame(root)
        frame_configuracoes.place(x=10, y=145)

        label_configuracoes = tk.Label(frame_configuracoes, text="Configurações:")
        label_configuracoes.pack(side=tk.LEFT)

        # Linhas Cabeçalho
        frame_linhas_cabecalho = tk.Frame(root)
        frame_linhas_cabecalho.place(x=114, y=128)

        label_linhas_cabecalho = tk.Label(frame_linhas_cabecalho, text="Linhas de Cabeçalho:")
        label_linhas_cabecalho.pack()

        # ComboBox para selecionar a Entrada Linhas Cabeçalho
        self.combo_entrada_linhas_cabecalho = ttk.Combobox(frame_linhas_cabecalho, values=list(range(1, 10)), width=16)
        self.combo_entrada_linhas_cabecalho.set(0)  # Defina o valor padrão como 0
        self.combo_entrada_linhas_cabecalho.pack(side=tk.LEFT, padx=20)

        # Linhas Rodapé
        frame_linhas_rodape = tk.Frame(root)
        frame_linhas_rodape.place(x=279, y=128)

        label_linhas_rodape = tk.Label(frame_linhas_rodape, text="Linhas de Rodapé:")
        label_linhas_rodape.pack()

        # ComboBox para selecionar a Entrada Linhas Rodapé
        self.combo_entrada_linhas_rodape = ttk.Combobox(frame_linhas_rodape, values=list(range(1, 10)), width=16)
        self.combo_entrada_linhas_rodape.set(0)  # Defina o valor padrão como 0
        self.combo_entrada_linhas_rodape.pack(side=tk.LEFT, padx=10)

        # Dividir Arquivo
        self.botao_dividir = tk.Button(root, width=20, text="Dividir Arquivo", fg='blue', command=self.dividir_arquivo)
        self.botao_dividir.place(x=440, y=145)
        # self.botao_dividir.pack()     


    def configurar_eventos(self, controller):
        self.botao_dividir.config(command=controller.dividir_arquivo)
        self.botao_selecionar_arquivo_original.config(command=controller.selecionar_arquivo_original)
        self.botao_selecionar_diretorio_saida.config(command=controller.selecionar_diretorio_saida)
        # self.botao_sair.config(command=controller.sair_programa)

    def get_num_partes(self):
        return self.combo_num_partes.get()

    def get_arquivo_original(self):
        return self.entrada_arquivo_original.get()

    def get_pasta_saida(self):
        return self.entrada_diretorio_saida.get()

    def get_num_linhas_cabecalho(self):
        return self.combo_entrada_linhas_cabecalho.get()

    def get_num_linhas_rodape(self):
        return self.combo_entrada_linhas_rodape.get()

    def mostrar_status(self, status):
        self.label_status.config(text=status)

    def selecionar_arquivo_original(self):
        self.controller.selecionar_arquivo_original()

    def selecionar_diretorio_saida(self):
        self.controller.selecionar_diretorio_saida()    

    def dividir_arquivo(self):
        self.controller.dividir_arquivo()   

    



