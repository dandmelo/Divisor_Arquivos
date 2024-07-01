# model.py

import math
import os
import pathlib
from tkinter import messagebox
import view

def dividir_arquivo_por_linhas(arquivo_ret, num_partes, pasta_saida, num_linhas_cabecalho, num_linhas_rodape):

    # Verifique se o diretório do arquivo original está vazio e, se estiver, emita um alerta
    if not arquivo_ret:
        messagebox.showinfo("Ops!", "Favor, Selecione o Arquivo Original.")
        return

    # Ler todas as linhas do arquivo .ret
    with open(arquivo_ret, 'r') as arquivo:
        linhas = arquivo.readlines()

    if num_partes <= 1 or num_partes > 10:
        mensagem_partes = f"O Número de Partes Deve Estar Entre 2 e 10."
        messagebox.showinfo("Ops!", mensagem_partes)
        return

    # Calcular o tamanho do corpo (linhas entre cabeçalho e rodapé)
    tamanho_corpo = len(linhas) - num_linhas_cabecalho - num_linhas_rodape

    if num_linhas_cabecalho == 0 and num_linhas_rodape == 0:
        num_linhas_por_parte = math.ceil(len(linhas) / num_partes)
    else:
        # Calcular o número de linhas que cada parte do corpo deve ter
        num_linhas_por_parte = math.ceil(tamanho_corpo / num_partes)

    # Calcular o número de linhas extras que sobram após a divisão igual
    linhas_extras = tamanho_corpo % num_partes
    # print('Linhas Extras Após a Divisão Igual:',linhas_extras,'\n')

    # Criar um dicionário para rastrear as linhas já usadas em cada parte
    partes_usadas = {i: [] for i in range(num_partes)}

    # Inicializar variáveis para manter o controle da parte atual e do índice da linha
    parte_atual = 0
    indice_linha = num_linhas_cabecalho

    # Verifique se o diretório de saída está vazio e, se estiver, defina-o como o diretório do arquivo original
    if not pasta_saida:
        pasta_saida = os.path.dirname(arquivo_ret)
        mensagem_pasta_saida = messagebox.askyesno("Atenção", f"As Partes Serão Geradas no Diretório do Arquivo Original. Deseja Continuar?")
        if mensagem_pasta_saida:
            print("Sim")
            return dividir_arquivo_por_linhas(arquivo_ret, num_partes, pasta_saida, num_linhas_cabecalho, num_linhas_rodape)
        else:
            print("Não")
            return pasta_saida

    # Criar uma pasta para salvar as partes
    os.makedirs(pasta_saida, exist_ok=True)

    # Obter o nome do arquivo sem o caminho
    nome_arquivo = os.path.basename(arquivo_ret)

    # Obter o nome do arquivo sem a extensão
    p = pathlib.Path(nome_arquivo)

    # Obter somente a extensão do arquivo
    extensao_arquivo = pathlib.Path(nome_arquivo).suffix

    # Criar as partes do arquivo
    for i in range(num_partes):
        parte_atual = i
        parte_atual_linhas = []

        # Preencher a parte atual com linhas do corpo
        while len(parte_atual_linhas) < num_linhas_por_parte and indice_linha < len(linhas) - num_linhas_rodape:
            linha = linhas[indice_linha]

            # Verificar se a linha já foi usada em partes anteriores
            if linha not in partes_usadas[parte_atual]:
                parte_atual_linhas.append(linha)
                partes_usadas[parte_atual].append(linha)

            # Mover para a próxima linha
            indice_linha += 1

            # Voltar para a primeira parte quando todas as partes forem preenchidas
            if parte_atual == num_partes - 1:
                parte_atual = 0
            else:
                parte_atual += 1

        # Escrever a parte atual em um arquivo
        # A propriedade stem retorna o nome do arquivo sem a extensão
        nome_arquivo_parte = os.path.join(pasta_saida, p.stem + f'_{i + 1}'+ extensao_arquivo)

        with open(nome_arquivo_parte, 'w') as arquivo_parte:
            if num_linhas_cabecalho > 0:
                arquivo_parte.writelines(linhas[:num_linhas_cabecalho])
            arquivo_parte.writelines(parte_atual_linhas)
            if num_linhas_rodape > 0:
                arquivo_parte.writelines(linhas[-num_linhas_rodape:])

        print(f'Parte {i + 1} escrita em {nome_arquivo_parte}')
       

    mensagem_sucesso = f"O Arquivo foi Dividido em {num_partes} Partes com Sucesso^^"
    messagebox.showinfo("Sucesso!", mensagem_sucesso)



