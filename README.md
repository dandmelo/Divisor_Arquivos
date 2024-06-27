# Divisor_Arquivos (.RET/.TXT)

Este projeto foi criado no padrão de arquitetura de software MVC (Model-View-Controller). Surgiu da necessidade de dividir os arquivos de retorno bancário (extensão.RET) recebidos do Banco do Brasil pelo setor financeiro da empresa em que trabalhava. Em cada parte dividida faz-se necessário incluir sempre o cabeçalho e rodapé. Além dos arquivos com a extensão .RET, é possível também dividir arquivos com a extensão .TXT.

Possui uma interface gráficas, onde é possível:

1. Escolher o números de partes da divisão do arquivo;
2. Selecionar o arquivo a ser dividido (arquivo original);
3. Selecionar o diretório de saída das partes divididas;
4. Escolher a quantidade de linhas de cabeçalho;
5. Escolher a quantidade de linhas de rodapé.

## Ferramentas e Bibliotecas Utilizadas
* Python
* Pycharm
* Tkinter
* OS
* Math
* Pathlib
* Messagebox
* Filedialog

## Como Utilizar
O uso é simples e amigável.
Você escolhe a quantidade de partes que deseja dividir o arquivo, seleciona o arquivo a ser dividido, seleciona o diretório de saída (caso não informe este, as partes divididas serão salvas no mesmo diretório do arquivo original - uma mensagem será aberta para sua confirmação). Por último, informe a quantidade de linhas do cabeçalho e rodapé e clique no botão "Dividir Arquivo".
